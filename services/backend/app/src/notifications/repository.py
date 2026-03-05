from sqlalchemy import select, func, update

from app.src.base.repository import BaseRepository
from app.src.database import async_session_maker
from app.src.notifications.models import Notification
from app.src.notifications.schemas import NotificationSchema


class NotificationRepository(BaseRepository[Notification]):

    def __init__(self):
        super().__init__(
            model=Notification,
            schema=NotificationSchema
        )

    async def list_by_user(self, user_uuid: str) -> list[Notification]:
        async with async_session_maker() as session:
            result = await session.execute(
                select(NotificationSchema)
                .where(NotificationSchema.user_uuid == user_uuid)
                .order_by(NotificationSchema.created_at.desc())
            )
            return [self.model.model_validate(r.__dict__) for r in result.scalars().all()]

    async def unread_count(self, user_uuid: str) -> int:
        async with async_session_maker() as session:
            result = await session.execute(
                select(func.count())
                .select_from(NotificationSchema)
                .where(
                    NotificationSchema.user_uuid == user_uuid,
                    NotificationSchema.is_read == False,
                )
            )
            return result.scalar() or 0

    async def mark_read(self, uuid: str) -> bool:
        async with async_session_maker() as session:
            result = await session.execute(select(NotificationSchema).where(NotificationSchema.uuid == uuid))
            row = result.scalar_one_or_none()
            if not row:
                return False
            row.is_read = True
            await session.commit()
            return True

    async def mark_all_read(self, user_uuid: str) -> None:
        async with async_session_maker() as session:
            await session.execute(
                update(NotificationSchema)
                .where(
                    NotificationSchema.user_uuid == user_uuid,
                    NotificationSchema.is_read == False,
                )
                .values(is_read=True)
            )
            await session.commit()
