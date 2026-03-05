from app.src.base.model import CustomModel, TimestampModel, OwnerModel


class Notification(CustomModel, TimestampModel, OwnerModel):
    user_uuid: str
    title: str
    body: str
    notification_type: str
    reference_uuid: str | None = None
    is_read: bool = False
