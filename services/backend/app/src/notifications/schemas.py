from sqlalchemy import Boolean, Column, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.src.database import Base
from app.src.base.schema import CustomSchema, TimestampSchema, OwnerSchema


class NotificationSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "notifications__notification"

    user_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    notification_type = Column(String(50), nullable=False)
    reference_uuid = Column(PG_UUID(as_uuid=True), nullable=True)
    is_read = Column(Boolean, default=False, nullable=False)
