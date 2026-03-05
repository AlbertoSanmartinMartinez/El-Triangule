from app.src.base.controller import BaseController
from app.src.events.models import Event, EventAttendee
from app.src.events.repository import EventRepository, EventAttendeeRepository
from app.src.base.error import NotFoundError, ConflictError


class EventController(BaseController[Event]):

    def __init__(self):
        super().__init__(
            repository=EventRepository(),
            event=None,
            cache=None
        )
        self.attendee_repo = EventAttendeeRepository()

    async def register_attendee(self, event_uuid: str, user_uuid: str) -> EventAttendee:
        await self.detail(event_uuid)
        existing = await self.attendee_repo.get_attendee(event_uuid, user_uuid)
        if existing:
            raise ConflictError("Already registered")
        attendee = EventAttendee(event_uuid=event_uuid, user_uuid=user_uuid, created_by=user_uuid)
        return await self.attendee_repo.create(attendee)

    async def unregister_attendee(self, event_uuid: str, user_uuid: str) -> None:
        if not await self.attendee_repo.unregister(event_uuid, user_uuid):
            raise NotFoundError("Registration not found")
