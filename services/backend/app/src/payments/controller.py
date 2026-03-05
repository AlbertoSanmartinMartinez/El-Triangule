from uuid import uuid4

from fastapi import Request

from app.src.base.controller import BaseController
from app.src.payments.models import Payment
from app.src.payments.repository import PaymentRepository
from app.src.base.error import NotFoundError


class PaymentController(BaseController[Payment]):

    def __init__(self):
        super().__init__(
            repository=PaymentRepository(),
            event=None,
            cache=None
        )

    async def create(self, item: Payment, request: Request | None = None) -> Payment:
        item.status = "completed"
        item.transaction_id = f"mock_{uuid4().hex[:12]}"
        return await self.repository.create(item)

    async def list_by_user(self, user_uuid: str) -> list[Payment]:
        return await self.repository.list_by_user(user_uuid)

    async def refund(self, uuid: str) -> Payment:
        payment = await self.repository.update_status(uuid, "refunded")
        if not payment:
            raise NotFoundError("Payment not found")
        return payment
