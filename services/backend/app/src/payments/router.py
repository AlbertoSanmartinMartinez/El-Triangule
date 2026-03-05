from fastapi import Request, HTTPException

from app.src.base.router import BaseRouter
from app.src.base.error import AppError
from app.src.config import settings
from app.src.payments.models import Payment
from app.src.payments.controller import PaymentController

payment_router: BaseRouter[Payment] = BaseRouter(
    model=Payment,
    controller=PaymentController,
    prefix=f"/{settings.api_prefix}/payments/payment",
    tags=["Payment"],
)


@payment_router.router.post(
    "/{uuid}/refund",
    response_model=Payment,
    summary="Refund payment",
)
async def refund_payment(uuid: str) -> Payment:
    try:
        return await payment_router.controller.refund(uuid)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
