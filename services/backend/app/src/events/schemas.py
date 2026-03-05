from sqlalchemy import Column, Date, Float, String, Text, Time, ForeignKey, Enum as SA_Enum
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.src.database import Base
from app.src.base.schema import CustomSchema, TimestampSchema, OwnerSchema
from app.src.events.models import AttendeeStatus


class EventSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "events__event"

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=True)
    date = Column(Date, nullable=True)
    time = Column(Time, nullable=True)
    price = Column(Float, nullable=True)


class EventAttendeeSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "events__event_attendee"

    event_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("events__event.uuid"), nullable=False, index=True)
    user_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=False, index=True)
    status = Column(SA_Enum(AttendeeStatus, name="events__attendee_status", native_enum=True), default=AttendeeStatus.PENDING, nullable=False)
