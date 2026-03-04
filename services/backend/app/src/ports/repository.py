"""
Repository Port module
"""

from abc import abstractmethod
from typing import Dict, TypeVar, Generic, List, Optional, Any


T = TypeVar('T')

class RepositoryPort(Generic[T]):
    """Repository port interface"""
    
    @abstractmethod
    async def create(self, item: T) -> T:
        """Create a new item"""
        pass
    
    @abstractmethod
    async def list(self, filters: Optional[Dict[Any, Any]] = None) -> Dict[str, Any]:
        """List items with optional filters"""
        pass
    
    @abstractmethod
    async def detail(self, pk: str, include_relations: Optional[List[str]] = None) -> Optional[T]:
        """Get item by primary key"""
        pass
    
    @abstractmethod
    async def update(self, pk: str, item_update: T) -> T:
        """Update an item"""
        pass
    
    @abstractmethod
    async def update_partial(self, pk: str, item_update: T) -> None:
        """Update an item without returning the validated model (for partial updates)"""
        pass
    
    @abstractmethod
    async def delete(self, pk: str) -> None:
        """Delete an item"""
        pass 