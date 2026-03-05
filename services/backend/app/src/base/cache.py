from typing import TypeVar, Generic, Optional, Type

from pydantic import BaseModel

from app.src.ports.cache import CachePort

T = TypeVar('T', bound=BaseModel)


class BaseCache(CachePort[T], Generic[T]):

    def __init__(self, model: Type[T]):
        self.model = model

    async def get(self, key: str) -> Optional[T]:
        raise NotImplementedError("Cache get is not implemented yet.")

    async def set(self, key: str, data: T) -> None:
        raise NotImplementedError("Cache set is not implemented yet.")

    async def delete(self, key: str) -> None:
        raise NotImplementedError("Cache delete is not implemented yet.")
