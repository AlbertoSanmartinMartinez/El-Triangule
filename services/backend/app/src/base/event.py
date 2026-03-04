import asyncio
from typing import TypeVar, Generic, Any, Type, Optional

from kafka_client_python import (
    AsyncKafkaProducer,
    AsyncKafkaConsumer,
    default_value_serializer,
    default_key_serializer,
)

from src.ports.event import EventPort
from src.settings import settings

T = TypeVar('T')

# Shared producer (created once on startup and reused across requests)
_producer: AsyncKafkaProducer | None = None
_producer_lock = asyncio.Lock()
_producer_started = False


async def init_event_producer() -> AsyncKafkaProducer:
    """
    Create and start a shared AsyncKafkaProducer once (e.g., on FastAPI startup).
    """

    global _producer_started, _producer

    async with _producer_lock:
        
        if _producer is None:
            _producer = AsyncKafkaProducer(
                bootstrap_servers=settings.kafka_server,
                environment=settings.environment,
                value_serializer=default_value_serializer,
                key_serializer=default_key_serializer,
            )
        
        if not _producer_started:
            await _producer.start()
            _producer_started = True

    return _producer


async def shutdown_event_producer() -> None:
    """Flush pending messages on application shutdown without per-request flushes."""
    global _producer_started
    async with _producer_lock:
        if _producer and _producer_started:
            await _producer.stop()
            _producer_started = False


class BaseEvent(EventPort[T], Generic[T]):
    """Base event class"""

    def __init__(
        self,
        model: Type[T],
    ):
        """..."""

        self.model = model
        self._producer: AsyncKafkaProducer | None = None

    async def _get_producer(self) -> AsyncKafkaProducer:
        """
        Retrieve the shared async Kafka producer (started once, reused per request).
        """

        if self._producer is None or not _producer_started:
            # Startup may have been skipped; ensure it's running.
            self._producer = await init_event_producer()

        return self._producer

    async def _get_consumer(self) -> AsyncKafkaConsumer:
        """
        Placeholder for consumer wiring. Pending implementation.
        """

        raise NotImplementedError("Kafka consumer is not implemented yet.")
    
    async def push(self, topic: Optional[str], data: Any) -> Optional[T]:
        """..."""

        if not topic:
            raise ValueError("Topic is required to publish an event")

        producer = await self._get_producer()
        
        # Fire-and-forget to keep API requests fast; rely on shared producer lifecycle.
        await producer.send(
            topic=topic,
            value=data,
            wait_for_delivery=False,
        )
        return None
    
    async def pull(self, topic: str) -> None:
        """Pending implementation for Kafka consumer."""

        raise NotImplementedError("Kafka consumer is not implemented yet.")