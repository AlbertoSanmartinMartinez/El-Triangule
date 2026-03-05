from sqlalchemy import Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class CustomSchema:
    uuid = Column(PG_UUID(as_uuid=True), primary_key=True)


class TimestampSchema:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class OwnerSchema:
    created_by = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=True)
