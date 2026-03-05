from fastapi import Request, HTTPException

from app.src.base.router import BaseRouter
from app.src.base.error import AppError
from app.src.config import settings
from app.src.notifications.models import Notification
from app.src.notifications.controller import NotificationController

notification_router: BaseRouter[Notification] = BaseRouter(
    model=Notification,
    controller=NotificationController,
    prefix=f"/{settings.api_prefix}/notifications/notification",
    tags=["Notification"],
)


@notification_router.router.get(
    "/unread-count",
    summary="Unread notifications count",
)
async def unread_count(request: Request):
    count = await notification_router.controller.unread_count(request.state.user_uuid)
    return {"count": count}


@notification_router.router.patch(
    "/{uuid}/read",
    summary="Mark notification as read",
)
async def mark_read(uuid: str):
    try:
        await notification_router.controller.mark_read(uuid)
        return {"status": "ok"}
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@notification_router.router.patch(
    "/read-all",
    summary="Mark all notifications as read",
)
async def mark_all_read(request: Request):
    await notification_router.controller.mark_all_read(request.state.user_uuid)
    return {"status": "ok"}
