from sqlalchemy import Column, ForeignKey, String, Text, Enum as SA_Enum
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.src.database import Base
from app.src.base.schema import CustomSchema, TimestampSchema, OwnerSchema
from app.src.messages.models import ConversationType, MemberRole


class ConversationSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "messages__conversation"

    name = Column(String(255), nullable=True)
    type = Column(SA_Enum(ConversationType, name="messages__conversation_type", native_enum=True), default=ConversationType.GROUP, nullable=False)
    image_url = Column(String(500), nullable=True)


class ConversationMemberSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "messages__conversation_member"

    conversation_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("messages__conversation.uuid"), nullable=False, index=True)
    user_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=False, index=True)
    role = Column(SA_Enum(MemberRole, name="messages__member_role", native_enum=True), default=MemberRole.MEMBER, nullable=False)


class ActiveConnectionSchema(CustomSchema, TimestampSchema, Base):
    __tablename__ = "messages__active_connection"

    conversation_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("messages__conversation.uuid"), nullable=False, index=True)
    user_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=False, index=True)


class MessageSchema(CustomSchema, TimestampSchema, OwnerSchema, Base):
    __tablename__ = "messages__message"

    conversation_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("messages__conversation.uuid"), nullable=False, index=True)
    sender_uuid = Column(PG_UUID(as_uuid=True), ForeignKey("auth__user.uuid"), nullable=False)
    content = Column(Text, nullable=False)
