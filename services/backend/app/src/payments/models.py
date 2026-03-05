from app.src.base.model import CustomModel, TimestampModel, OwnerModel


class Payment(CustomModel, TimestampModel, OwnerModel):
    user_uuid: str
    event_uuid: str
    amount: float
    currency: str = "EUR"
    payment_method: str
    status: str = "pending"
    transaction_id: str | None = None
