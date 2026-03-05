from app.src.base.controller import BaseController
from app.src.notifications.models import Notification
from app.src.notifications.repository import NotificationRepository
from app.src.base.error import NotFoundError


class NotificationController(BaseController[Notification]):

    def __init__(self):
        super().__init__(
            repository=NotificationRepository(),
            event=None,
            cache=None
        )

    async def list_by_user(self, user_uuid: str) -> list[Notification]:
        return await self.repository.list_by_user(user_uuid)

    async def unread_count(self, user_uuid: str) -> int:
        return await self.repository.unread_count(user_uuid)

    async def mark_read(self, uuid: str) -> None:
        if not await self.repository.mark_read(uuid):
            raise NotFoundError("Notification not found")

    async def mark_all_read(self, user_uuid: str) -> None:
        await self.repository.mark_all_read(user_uuid)


class NotificationService:

    _repository = NotificationRepository()

    @classmethod
    async def create(
        cls,
        user_uuid: str,
        title: str,
        body: str,
        notification_type: str,
        reference_uuid: str | None = None,
        created_by: str | None = None,
    ) -> Notification:
        notification = Notification(
            user_uuid=user_uuid,
            title=title,
            body=body,
            notification_type=notification_type,
            reference_uuid=reference_uuid,
            created_by=created_by,
        )
        return await cls._repository.create(notification)
