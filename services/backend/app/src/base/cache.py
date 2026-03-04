from typing import TypeVar, Generic, Optional, Type

from pydantic import BaseModel

from src.ports.cache import CachePort
from src.settings import settings
from src.databases import async_redis_client

T = TypeVar('T', bound=BaseModel)


class BaseCache(CachePort[T], Generic[T]):
    """Base cache class"""
    
    model: type[T]

    def __init__(
        self,
        model: Type[T]
    ):
        """..."""

        self.model = model
        # Namespace keys by model to avoid collisions across caches using same UUID
        self.namespace = getattr(model, "__name__", model.__class__.__name__)
        self.async_redis_client = async_redis_client

    async def get(self, key: str) -> Optional[T]:
        """Get item from cache"""

        key = f"{self.namespace}:{str(key)}"
        data = await self.async_redis_client.get(key)
        
        if data:
            try:
                return self.model.model_validate_json(data)
            except Exception:
                # If cache content is stale or malformed, ignore and let caller hit repository
                return None
        
        return None

    async def set(self, key: str, data: T) -> None:
        """Set item in cache"""

        key = f"{self.namespace}:{str(key)}"
        await self.async_redis_client.set(
            key,
            data.model_dump_json(by_alias=True),
            ex=settings.redis_ttl
        )

    async def delete(self, key: str) -> None:
        """Delete item from cache"""

        key = f"{self.namespace}:{str(key)}"
        await self.async_redis_client.delete(key)
