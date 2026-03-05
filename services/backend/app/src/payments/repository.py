from sqlalchemy import select

from app.src.base.repository import BaseRepository
from app.src.database import async_session_maker
from app.src.payments.models import Payment
from app.src.payments.schemas import PaymentSchema


class PaymentRepository(BaseRepository[Payment]):

    def __init__(self):
        super().__init__(
            model=Payment,
            schema=PaymentSchema
        )

    async def list_by_user(self, user_uuid: str) -> list[Payment]:
        async with async_session_maker() as session:
            result = await session.execute(
                select(PaymentSchema)
                .where(PaymentSchema.user_uuid == user_uuid)
                .order_by(PaymentSchema.created_at.desc())
            )
            return [self.model.model_validate(r.__dict__) for r in result.scalars().all()]

    async def update_status(self, uuid: str, status: str) -> Payment | None:
        async with async_session_maker() as session:
            result = await session.execute(select(PaymentSchema).where(PaymentSchema.uuid == uuid))
            row = result.scalar_one_or_none()
            if not row:
                return None
            row.status = status
            await session.commit()
            await session.refresh(row)
            return self.model.model_validate(row.__dict__)
