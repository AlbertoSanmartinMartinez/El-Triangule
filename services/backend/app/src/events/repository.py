from sqlalchemy import select, and_

from app.src.base.repository import BaseRepository
from app.src.database import async_session_maker
from app.src.events.models import Event, EventAttendee
from app.src.events.schemas import EventSchema, EventAttendeeSchema


class EventRepository(BaseRepository[Event]):

    def __init__(self):
        super().__init__(
            model=Event,
            schema=EventSchema
        )


class EventAttendeeRepository(BaseRepository[EventAttendee]):

    def __init__(self):
        super().__init__(
            model=EventAttendee,
            schema=EventAttendeeSchema
        )

    async def get_attendee(self, event_uuid: str, user_uuid: str) -> EventAttendee | None:
        async with async_session_maker() as session:
            result = await session.execute(
                select(EventAttendeeSchema).where(
                    and_(
                        EventAttendeeSchema.event_uuid == event_uuid,
                        EventAttendeeSchema.user_uuid == user_uuid,
                    )
                )
            )
            row = result.scalar_one_or_none()
            return self.model.model_validate(row.__dict__) if row else None

    async def unregister(self, event_uuid: str, user_uuid: str) -> bool:
        async with async_session_maker() as session:
            result = await session.execute(
                select(EventAttendeeSchema).where(
                    and_(
                        EventAttendeeSchema.event_uuid == event_uuid,
                        EventAttendeeSchema.user_uuid == user_uuid,
                    )
                )
            )
            row = result.scalar_one_or_none()
            if not row:
                return False
            await session.delete(row)
            await session.commit()
            return True
