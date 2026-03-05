from enum import Enum

from pydantic import BaseModel

from app.src.base.model import CustomModel, TimestampModel, OwnerModel


class ConversationType(str, Enum):
    GROUP = "group"
    INDIVIDUAL = "individual"


class Conversation(CustomModel, TimestampModel, OwnerModel):
    name: str | None = None
    type: ConversationType = ConversationType.GROUP
    image_url: str | None = None


class MemberRole(str, Enum):
    OWNER = "owner"
    MEMBER = "member"


class ConversationMember(CustomModel, TimestampModel, OwnerModel):
    conversation_uuid: str
    user_uuid: str
    role: MemberRole = MemberRole.MEMBER


class Message(CustomModel, TimestampModel, OwnerModel):
    conversation_uuid: str
    sender_uuid: str
    content: str


class ActiveConnection(CustomModel, TimestampModel):
    conversation_uuid: str
    user_uuid: str


class AddMemberRequest(BaseModel):
    user_uuid: str
