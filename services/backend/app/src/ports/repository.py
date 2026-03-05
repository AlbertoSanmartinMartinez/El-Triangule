from abc import abstractmethod
from typing import Dict, TypeVar, Generic, List, Optional, Any


T = TypeVar('T')

class RepositoryPort(Generic[T]):

    @abstractmethod
    async def create(self, item: T) -> T:
        pass

    @abstractmethod
    async def list(self, filters: Optional[Dict[Any, Any]] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def detail(self, pk: str, include_relations: Optional[List[str]] = None) -> Optional[T]:
        pass

    @abstractmethod
    async def update(self, pk: str, item_update: T) -> T:
        pass

    @abstractmethod
    async def update_partial(self, pk: str, item_update: T) -> None:
        pass

    @abstractmethod
    async def delete(self, pk: str) -> None:
        pass
