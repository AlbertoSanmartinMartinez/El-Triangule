import copy, json

from typing import List, Type, TypeVar, Generic, Any, Optional

from fastapi import APIRouter, status, Body, Query, HTTPException, Depends, Request

from pydantic import BaseModel, ValidationError, create_model

from src.ports.router import RouterPort
from src.base.controller import BaseController
from src.base.error import AppError
from src.ports.filtering import (
    FiltersInterface,
    ListResponse,
    OrderParams,
    PaginationParams,
    SearchParams,
)
from src.settings import settings
from src.base.mixins import SensitiveFieldsMixin

T = TypeVar('T', bound=BaseModel)


def FiltersInterfaceQuery(
    request: Request,
    filters: Optional[str] = Query(
        default=None,
        alias="filters",
        description="Legacy JSON string with the full filters payload",
        include_in_schema=False
    ),
    search: Optional[List[str]] = Query(
        default=None,
        alias="filters.search",
        description="Repeat per search condition. Value can be JSON or attribute:operator:value",
        include_in_schema=False
    ),
    include_relations: Optional[List[str]] = Query(
        default=None,
        alias="filters.include_relations",
        include_in_schema=False
    ),
    pagination_page: Optional[int] = Query(None, alias="filters.pagination.page", include_in_schema=False),
    pagination_num_items: Optional[int] = Query(None, alias="filters.pagination.num_items", include_in_schema=False),
    order_attribute: Optional[str] = Query(None, alias="filters.order.attribute", include_in_schema=False),
    order_direction: Optional[str] = Query(None, alias="filters.order.direction", include_in_schema=False),
) -> FiltersInterface:
    if filters:
        try:
            filters_data = json.loads(filters)
            if isinstance(filters_data, list):
                filters_data = {"search": filters_data}
            return FiltersInterface.model_validate(filters_data)
        except (json.JSONDecodeError, ValidationError) as exc:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid filters payload: {exc}"
            ) from exc

    def tokenize(key: str) -> List[str]:
        tokens: List[str] = []
        current = ""
        i = 0
        while i < len(key):
            char = key[i]
            if char == "[":
                if current:
                    tokens.append(current)
                    current = ""
                i += 1
                segment = ""
                while i < len(key) and key[i] != "]":
                    segment += key[i]
                    i += 1
                tokens.append(segment)
                i += 1
            elif char == ".":
                if current:
                    tokens.append(current)
                    current = ""
                i += 1
            else:
                current += char
                i += 1
        if current:
            tokens.append(current)
        return [token for token in tokens if token]

    def assign_value(container: Any, tokens: List[str], value: Any) -> None:
        token = tokens[0]
        last = len(tokens) == 1

        if token.isdigit():
            idx = int(token)
            if not isinstance(container, list):
                raise HTTPException(status_code=400, detail="Invalid deep filters payload")
            while len(container) <= idx:
                container.append(None)
            if last:
                container[idx] = value
                return
            next_is_index = tokens[1].isdigit()
            if container[idx] is None:
                container[idx] = [] if next_is_index else {}
            assign_value(container[idx], tokens[1:], value)
            return

        if last:
            container[token] = value
            return

        next_is_index = tokens[1].isdigit()
        existing = container.get(token)
        if existing is None:
            container[token] = [] if next_is_index else {}
        elif next_is_index and not isinstance(existing, list):
            container[token] = []
        elif not next_is_index and not isinstance(existing, dict):
            container[token] = {}

        assign_value(container[token], tokens[1:], value)

    deep_payload: dict[str, Any] = {}
    for key, value in request.query_params.multi_items():
        if not key.startswith("filters["):
            continue
        path = tokenize(key)
        if not path or path[0] != "filters":
            continue
        if len(path) == 1:
            continue
        if isinstance(deep_payload.get(path[1]), list) and not path[1].isdigit():
            pass
        assign_value(deep_payload, path[1:], value)

    if deep_payload:
        try:
            return FiltersInterface.model_validate(deep_payload)
        except ValidationError as exc:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid deep filters payload: {exc}"
            ) from exc

    search_params: List[SearchParams] = []
    for entry in search or []:
        try:
            parsed_entry = json.loads(entry)
        except json.JSONDecodeError:
            parts = entry.split(":", 2)
            if len(parts) != 3:
                raise HTTPException(
                    status_code=400,
                    detail="Search filters must use 'attribute:operator:value' or JSON format"
                )
            parsed_entry = {"attribute": parts[0], "operator": parts[1], "value": parts[2]}
        search_params.append(SearchParams(**parsed_entry))

    pagination = PaginationParams(
        page=pagination_page or 1,
        num_items=pagination_num_items or 50,
    )
    order = OrderParams(
        attribute=order_attribute or "uuid",
        direction=order_direction or "ASC",
    )

    return FiltersInterface(
        search=search_params,
        include_relations=include_relations or [],
        pagination=pagination,
        order=order
    )


class BaseRouter(RouterPort[T], Generic[T]):
    """Base router class"""

    def __init__(
        self,
        model: Type[T],
        controller: Type[BaseController[T]],
        prefix: str,
        tags: Any,
        authentication_required: bool = True,
        authorisation_required: bool = True,
        permissions: Optional[dict[str, List[str]]] = None,
        authentication_overrides: Optional[dict[str, dict[str, bool]]] = None,
        authorisation_overrides: Optional[dict[str, bool]] = None,
    ) -> None:
        """Initialize router with model and controller"""

        self.model = model
        self.controller = controller()
        self.router = APIRouter(prefix=prefix, tags=tags)
        self.authentication_required = authentication_required
        self.authorisation_required = authorisation_required
        self.permissions = permissions or {}
        self.authentication_overrides = authentication_overrides or {}
        self.authorisation_overrides = authorisation_overrides or {}
        
        # Create a partial model for updates
        # If the original model uses SensitiveFieldsMixin, the update_model should inherit it
        # so that sensitive fields are encrypted during validation
        fields = {}
        for field_name, field in model.__annotations__.items():
            fields[field_name] = (Optional[field], None)
        
        # Determine base class for update_model
        if issubclass(model, SensitiveFieldsMixin):
            # Create a proper base class that combines BaseModel with the mixin
            class SensitiveUpdateBase(SensitiveFieldsMixin, BaseModel):
                pass
            self.update_model = create_model(
                f"{model.__name__}Update",
                __base__=SensitiveUpdateBase,
                **fields
            )
        else:
            self.update_model = create_model(f"{model.__name__}Update", **fields)
        
        # Rebuild models to resolve forward references, merging namespaces from
        # the model's module and its package (helps with cross-module relations).
        model_module_name = model.__module__
        namespace: dict[str, Any] = {}
        if model_module_name:
            import sys
            module = sys.modules.get(model_module_name)
            if module:
                namespace.update(vars(module))
            # Try also the package namespace (e.g., 'src.auth.models')
            if "." in model_module_name:
                pkg_name = model_module_name.rsplit(".", 1)[0]
                pkg_module = sys.modules.get(pkg_name)
                if pkg_module:
                    namespace.update(vars(pkg_module))
        try:
            # Rebuild the primary model first (used as response_model)
            if namespace:
                self.model.model_rebuild(_types_namespace=namespace)
                self.update_model.model_rebuild(_types_namespace=namespace)
            else:
                self.model.model_rebuild()
                self.update_model.model_rebuild()
        except Exception:
            # Fallback to default rebuild if namespace strategy fails
            self.model.model_rebuild()
            self.update_model.model_rebuild()
        
        
        self._register_routes()

    def _inline_schema_refs(self, schema: dict[str, Any]) -> dict[str, Any]:
        """Replace local $ref references with inline definitions for parameters."""

        definitions = schema.pop("$defs", None) or schema.pop("definitions", None) or {}

        def resolve(node: Any) -> Any:
            if isinstance(node, dict):
                ref = node.get("$ref")
                if ref and ref.startswith("#/"):
                    key = ref.split("/")[-1]
                    if key in definitions:
                        return resolve(copy.deepcopy(definitions[key]))
                return {k: resolve(v) for k, v in node.items()}
            if isinstance(node, list):
                return [resolve(item) for item in node]
            return node

        return resolve(schema)

    def get_router(self):
        """Get the FastAPI router instance"""
        return self.router

    def _register_routes(self) -> None:
        """Register all routes"""

        # Lazy import to avoid circular dependency issues
        from src.auth.decorators import require_authorisation, require_authentication

        def build_service_name() -> str:
            tokens = [p for p in self.router.prefix.split("/") if p]
            if tokens and tokens[0] == getattr(settings, "api_prefix", "api"):
                if len(tokens) > 1:
                    return tokens[1]
                return tokens[0]
            return tokens[0] if tokens else "service"

        service_name = build_service_name()

        def model_has_field(field_name: str) -> bool:
            model_fields = getattr(self.model, "model_fields", None)
            if isinstance(model_fields, dict):
                return field_name in model_fields
            return False

        def build_dependencies(
            action: str,
            instance_param: str | None = None,
            token_required: bool = True,
            tenant_required: bool = True,
        ):
            
            deps = []
            
            action_auth = self.authentication_overrides.get(action, {})
            token_required = action_auth.get("token_required", token_required)
            tenant_required = action_auth.get("tenant_required", tenant_required)

            if self.authentication_required:
                deps.append(
                    Depends(
                        require_authentication(
                            token_required=token_required,
                            tenant_required=tenant_required,
                        )
                    )
                )
            action_authorisation_required = self.authorisation_overrides.get(action, True)
            if self.authorisation_required and action_authorisation_required:
                deps.append(
                    Depends(
                        require_authorisation(
                            authorisation_required=self.authorisation_required,
                            token_required=token_required,
                            tenant_required=tenant_required,
                            action=action,
                            service=service_name,
                            model=self.model.__name__,
                            instance_param=instance_param,
                            custom_permissions=self.permissions.get(action, []),
                        )
                    )
                )
                
            return deps

        @self.router.post( # type: ignore
            "",
            response_model=self.model,
            status_code=status.HTTP_201_CREATED,
            dependencies=build_dependencies(action="create"),
        )
        async def create(request: Request, item: self.model = Body(...)) -> T:
            try:
                if model_has_field("tenant_id") and getattr(request.state, "tenant_id", None):
                    setattr(item, "tenant_id", request.state.tenant_id)
                return await self.create(item, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        filters_schema = self._inline_schema_refs(FiltersInterface.model_json_schema())

        @self.router.get( # type: ignore
            "",
            response_model=ListResponse[self.model],
            openapi_extra={
                "parameters": [
                    {
                        "name": "filters",
                        "in": "query",
                        "required": False,
                        "style": "deepObject",
                        "explode": True,
                        "schema": filters_schema,
                        "description": "FiltersInterface encoded as a deep object (filters[...])"
                    }
                ]
            },
            dependencies=build_dependencies(action="list"),
        )
        async def list(request: Request, filters: FiltersInterface = Depends(FiltersInterfaceQuery)) -> ListResponse[T]:
            try:
                # Apply tenant filter if available and model has tenant_id
                if model_has_field("tenant_id") and getattr(request.state, "tenant_id", None):
                    filters.search.append(
                        SearchParams(attribute="tenant_id", operator="eq", value=request.state.tenant_id)
                    )
                return await self.list(filters, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get( # type: ignore
            "/{pk}",
            response_model=self.model,
            dependencies=build_dependencies(action="detail", instance_param="pk"),
        )
        async def detail(
            request: Request,
            pk: str,
            include_relations: Optional[List[str]] = Query(default=None),
        ) -> T:
            item = await self.detail(pk, include_relations=include_relations, request=request)
            if model_has_field("tenant_id") and getattr(request.state, "tenant_id", None):
                if getattr(item, "tenant_id", None) != request.state.tenant_id:
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
            return item

        @self.router.patch( # type: ignore
            "/{pk}",
            response_model=self.model,
            dependencies=build_dependencies(action="update", instance_param="pk"),
        )
        async def update(request: Request, pk: str, item_update: Any = Body(...)) -> T:
            try:
                return await self.update(pk, item_update, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.delete( # type: ignore
            "/{pk}",
            status_code=status.HTTP_204_NO_CONTENT,
            dependencies=build_dependencies(action="delete", instance_param="pk"),
        )
        async def delete(request: Request, pk: str) -> None:
            try:
                await self.delete(pk, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def create(self, item: T, request: Request | None = None) -> T:
        """Create endpoint handler"""

        return await self.controller.create(item, request=request)

    async def list(self, filters: FiltersInterface, request: Request | None = None) -> ListResponse[T]:
        """List endpoint handler with optional filters"""
        
        return await self.controller.list(filters=filters, request=request)

    async def detail(self, pk: str, include_relations: Optional[List[str]] = None, request: Request | None = None) -> T:
        """Detail endpoint handler"""

        return await self.controller.detail(pk, include_relations=include_relations, request=request)

    async def update(self, pk: str, item_update: Any, request: Request | None = None) -> T:
        """Update endpoint handler"""
        
        update_data = self.update_model(**item_update)
        return await self.controller.update(pk, update_data, request=request)

    async def delete(self, pk: str, request: Request | None = None) -> None:
        """Delete endpoint handler"""

        await self.controller.delete(pk, request=request)

