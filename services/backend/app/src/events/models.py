import datetime as dt
from enum import Enum

from app.src.base.model import CustomModel, TimestampModel, OwnerModel


class AttendeeStatus(str, Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    PENDING = "pending"


class Event(CustomModel, TimestampModel, OwnerModel):
    title: str
    description: str | None = None
    location: str | None = None
    date: dt.date | None = None
    time: dt.time | None = None
    price: float | None = None


class EventAttendee(CustomModel, TimestampModel, OwnerModel):
    event_uuid: str
    user_uuid: str
    status: AttendeeStatus = AttendeeStatus.PENDING
