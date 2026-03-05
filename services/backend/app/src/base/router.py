import copy, json

from typing import List, Type, TypeVar, Generic, Any, Optional

from fastapi import APIRouter, status, Body, Query, HTTPException, Depends, Request

from pydantic import BaseModel, ValidationError, create_model

from app.src.ports.router import RouterPort
from app.src.base.controller import BaseController
from app.src.base.error import AppError
from app.src.ports.filtering import (
    FiltersInterface,
    ListResponse,
    OrderParams,
    PaginationParams,
    SearchParams,
)

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

    def __init__(
        self,
        model: Type[T],
        controller: Type[BaseController[T]],
        prefix: str,
        tags: Any,
    ) -> None:
        self.model = model
        self.controller = controller()
        self.router = APIRouter(prefix=prefix, tags=tags)

        fields = {}
        for field_name, field in model.__annotations__.items():
            fields[field_name] = (Optional[field], None)

        self.update_model = create_model(f"{model.__name__}Update", **fields)

        model_module_name = model.__module__
        namespace: dict[str, Any] = {}
        if model_module_name:
            import sys
            module = sys.modules.get(model_module_name)
            if module:
                namespace.update(vars(module))
            if "." in model_module_name:
                pkg_name = model_module_name.rsplit(".", 1)[0]
                pkg_module = sys.modules.get(pkg_name)
                if pkg_module:
                    namespace.update(vars(pkg_module))
        try:
            if namespace:
                self.model.model_rebuild(_types_namespace=namespace)
                self.update_model.model_rebuild(_types_namespace=namespace)
            else:
                self.model.model_rebuild()
                self.update_model.model_rebuild()
        except Exception:
            self.model.model_rebuild()
            self.update_model.model_rebuild()

        self._register_routes()

    def _inline_schema_refs(self, schema: dict[str, Any]) -> dict[str, Any]:
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
        return self.router

    def _register_routes(self) -> None:

        @self.router.post(
            "",
            response_model=self.model,
            status_code=status.HTTP_201_CREATED,
        )
        async def create(request: Request, item: self.model = Body(...)) -> T:
            try:
                return await self.create(item, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        filters_schema = self._inline_schema_refs(FiltersInterface.model_json_schema())

        @self.router.get(
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
        )
        async def list(request: Request, filters: FiltersInterface = Depends(FiltersInterfaceQuery)) -> ListResponse[T]:
            try:
                return await self.list(filters, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get(
            "/{pk}",
            response_model=self.model,
        )
        async def detail(
            request: Request,
            pk: str,
            include_relations: Optional[List[str]] = Query(default=None),
        ) -> T:
            return await self.detail(pk, include_relations=include_relations, request=request)

        @self.router.patch(
            "/{pk}",
            response_model=self.model,
        )
        async def update(request: Request, pk: str, item_update: Any = Body(...)) -> T:
            try:
                return await self.update(pk, item_update, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.delete(
            "/{pk}",
            status_code=status.HTTP_204_NO_CONTENT,
        )
        async def delete(request: Request, pk: str) -> None:
            try:
                await self.delete(pk, request=request)
            except AppError as e:
                raise HTTPException(status_code=e.status_code, detail=e.detail)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def create(self, item: T, request: Request | None = None) -> T:
        return await self.controller.create(item, request=request)

    async def list(self, filters: FiltersInterface, request: Request | None = None) -> ListResponse[T]:
        return await self.controller.list(filters=filters, request=request)

    async def detail(self, pk: str, include_relations: Optional[List[str]] = None, request: Request | None = None) -> T:
        return await self.controller.detail(pk, include_relations=include_relations, request=request)

    async def update(self, pk: str, item_update: Any, request: Request | None = None) -> T:
        update_data = self.update_model(**item_update)
        return await self.controller.update(pk, update_data, request=request)

    async def delete(self, pk: str, request: Request | None = None) -> None:
        await self.controller.delete(pk, request=request)
