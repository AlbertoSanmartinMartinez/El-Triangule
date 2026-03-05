from sqlalchemy import select, and_

from app.src.base.repository import BaseRepository
from app.src.database import async_session_maker
from app.src.messages.models import Conversation, ConversationMember, Message, ActiveConnection
from app.src.messages.schemas import ConversationSchema, ConversationMemberSchema, MessageSchema, ActiveConnectionSchema


class ConversationRepository(BaseRepository[Conversation]):

    def __init__(self):
        super().__init__(
            model=Conversation,
            schema=ConversationSchema
        )


class MemberRepository(BaseRepository[ConversationMember]):

    def __init__(self):
        super().__init__(
            model=ConversationMember,
            schema=ConversationMemberSchema
        )

    async def remove(self, conversation_uuid: str, user_uuid: str) -> bool:
        async with async_session_maker() as session:
            result = await session.execute(
                select(ConversationMemberSchema).where(
                    and_(
                        ConversationMemberSchema.conversation_uuid == conversation_uuid,
                        ConversationMemberSchema.user_uuid == user_uuid,
                    )
                )
            )
            row = result.scalar_one_or_none()
            if not row:
                return False
            await session.delete(row)
            await session.commit()
            return True


class ActiveConnectionRepository(BaseRepository[ActiveConnection]):

    def __init__(self):
        super().__init__(
            model=ActiveConnection,
            schema=ActiveConnectionSchema
        )

    async def connect(self, conversation_uuid: str, user_uuid: str) -> ActiveConnection:
        connection = ActiveConnection(conversation_uuid=conversation_uuid, user_uuid=user_uuid)
        return await self.create(connection)

    async def disconnect(self, conversation_uuid: str, user_uuid: str) -> None:
        async with async_session_maker() as session:
            result = await session.execute(
                select(ActiveConnectionSchema).where(
                    and_(
                        ActiveConnectionSchema.conversation_uuid == conversation_uuid,
                        ActiveConnectionSchema.user_uuid == user_uuid,
                    )
                )
            )
            row = result.scalar_one_or_none()
            if row:
                await session.delete(row)
                await session.commit()


class MessageRepository(BaseRepository[Message]):

    def __init__(self):
        super().__init__(
            model=Message,
            schema=MessageSchema
        )
