from typing import TypeVar, Generic, Any, Type, Optional

from app.src.ports.event import EventPort

T = TypeVar('T')


class BaseEvent(EventPort[T], Generic[T]):

    def __init__(self, model: Type[T]):
        self.model = model

    async def push(self, topic: Optional[str], data: Any) -> Optional[T]:
        raise NotImplementedError("Event push is not implemented yet.")

    async def pull(self, topic: str) -> None:
        raise NotImplementedError("Event pull is not implemented yet.")
