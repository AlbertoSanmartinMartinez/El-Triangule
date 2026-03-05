from fastapi import Request, HTTPException, status

from app.src.base.router import BaseRouter
from app.src.base.error import AppError
from app.src.config import settings
from app.src.events.models import Event
from app.src.events.controller import EventController

event_router: BaseRouter[Event] = BaseRouter(
    model=Event,
    controller=EventController,
    prefix=f"/{settings.api_prefix}/events/event",
    tags=["Event"],
)


@event_router.router.post(
    "/{uuid}/register",
    status_code=status.HTTP_201_CREATED,
    summary="Register to event",
)
async def register_event(uuid: str, request: Request):
    try:
        return await event_router.controller.register_attendee(uuid, request.state.user_uuid)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@event_router.router.delete(
    "/{uuid}/register",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Unregister from event",
)
async def unregister_event(uuid: str, request: Request):
    try:
        await event_router.controller.unregister_attendee(uuid, request.state.user_uuid)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
