from typing import TypeVar, Generic, Optional, Any, List

from fastapi import Request

from pydantic import BaseModel, ValidationError

from src.ports.repository import RepositoryPort
from src.ports.cache import CachePort
from src.ports.event import EventPort
from src.ports.filtering import FiltersInterface, ListResponse
from src.base.error import BadRequestError

T = TypeVar('T', bound=BaseModel)


class BaseController(Generic[T]):
    """Base controller class"""

    def __init__(
        self,
        repository: RepositoryPort[T] | None = None,
        cache: CachePort[T] | None = None,
        event: EventPort[T] | None = None,
    ):
        """..."""

        self.repository = repository
        self.cache = cache
        self.event = event

    async def list(self, filters: Optional[Any] = None, request: Request | None = None) -> ListResponse[T]:
        """List all items applying filters, pagination and ordering."""
        
        if self.repository is None:
            raise ValueError("Repository is not configured")
        
        try:
            filters_payload = FiltersInterface.from_raw(filters)
        except (ValueError, ValidationError) as exc:
            raise BadRequestError(str(exc)) from exc
        include_relations = filters_payload.include_relations.copy()
        repo_filters = filters_payload.model_copy(update={"include_relations": []})
        
        result = await self.repository.list(repo_filters)
        
        if include_relations and result["items"]:
            result["items"] = await self._load_relations(result["items"], include_relations)
        
        model_type = getattr(self.repository, "model", BaseModel)
        response_model = ListResponse[model_type]
        return response_model.model_validate(result)

    async def detail(self, pk: str, include_relations: Optional[List[str]] = None, request: Request | None = None) -> T:
        """Get item by primary key"""

        # Only use cache when no relations are requested
        # Relations are dynamic and should not be cached with the base item
        if self.cache is not None and not include_relations:
            cached_item = await self.cache.get(pk)
            if cached_item:
                return cached_item

        if self.repository is None:
            raise ValueError("Repository is not configured")
        item = await self.repository.detail(pk, include_relations=include_relations)
        
        if item is None:
            raise ValueError(f"Item with pk {pk} not found")
        
        if include_relations:
            enriched_items = await self._load_relations([item], include_relations)
            item = enriched_items[0]
        
        # Only cache items without relations to avoid stale relation data
        if self.cache is not None and not include_relations:
            await self.cache.set(pk, item)

        return item

    async def create(self, item: T, request: Request | None = None) -> T:
        """Create new item"""

        if self.repository is None:
            raise ValueError("Repository is not configured")
        item = await self.repository.create(item)

        if self.cache is not None:
            await self.cache.set(
                getattr(item, getattr(item, "pk_field")),
                item
            )

        if self.event is not None:
            await self.event.push(f"{self.event.model.__name__}.create", item.model_dump())

        return item

    async def update(self, pk: str, item_update: T, request: Request | None = None) -> T:
        """Update item"""

        if self.repository is None:
            raise ValueError("Repository is not configured")
        item = await self.repository.update(pk, item_update)
        
        if self.cache is not None:
            await self.cache.set(pk, item)
        if self.event is not None:
            await self.event.push(f"{self.event.model.__name__}.update", item.model_dump())

        return item

    async def delete(self, pk: str, request: Request | None = None) -> None:
        """Delete item"""

        if self.repository is None:
            raise ValueError("Repository is not configured")
        await self.repository.delete(pk)
        
        if self.cache is not None:
            await self.cache.delete(pk)
        if self.event is not None:
            await self.event.push(f"{self.event.model.__name__}.delete", pk)

    async def _load_relations(self, items: List[T], include_relations: List[str]) -> List[T]:
        """Load dynamic relations declared via include_relations."""
        
        if self.repository is None:
            return items
        
        schema = getattr(self.repository, "schema", None)
        for relation in include_relations:
            method_name = f"get_{relation}"
            if not hasattr(self.repository, method_name):
                if schema is not None and hasattr(schema, relation):
                    continue
                raise BadRequestError(f"Relation '{relation}' is not supported")
            loader = getattr(self.repository, method_name)
            for idx, item in enumerate(items):
                relation_data = await loader(item)
                # Set the relation attribute on the item
                if hasattr(item, relation):
                    setattr(item, relation, relation_data)
        
        return items
