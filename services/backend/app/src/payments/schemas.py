from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.src.database import Base
from app.src.base.schema import CustomSchema, TimestampSchema, OwnerSchema


class PaymentSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "payments__payment"

    user_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=False, index=True)
    event_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("events__event.uuid"), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default="EUR", nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(50), default="pending", nullable=False)
    transaction_id = Column(String(255), nullable=True)
