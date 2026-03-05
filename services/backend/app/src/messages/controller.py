from fastapi import Request

from app.src.base.controller import BaseController
from app.src.messages.models import Conversation, ConversationMember, Message, MemberRole, ActiveConnection
from app.src.messages.repository import ConversationRepository, MemberRepository, MessageRepository, ActiveConnectionRepository
from app.src.base.error import NotFoundError


class ConversationController(BaseController[Conversation]):

    def __init__(self):
        super().__init__(
            repository=ConversationRepository(),
            event=None,
            cache=None
        )
        self.member_repo = MemberRepository()

    async def create(self, item: Conversation, request: Request | None = None) -> Conversation:
        creator_uuid = request.state.user_uuid if request else None
        item.created_by = creator_uuid
        created = await self.repository.create(item)
        member = ConversationMember(
            conversation_uuid=str(created.uuid),
            user_uuid=creator_uuid,
            role=MemberRole.OWNER,
            created_by=creator_uuid,
        )
        await self.member_repo.create(member)
        return created

    async def add_member(self, conversation_uuid: str, user_uuid: str, created_by: str) -> ConversationMember:
        member = ConversationMember(
            conversation_uuid=conversation_uuid,
            user_uuid=user_uuid,
            created_by=created_by,
        )
        return await self.member_repo.create(member)

    async def remove_member(self, conversation_uuid: str, user_uuid: str) -> None:
        if not await self.member_repo.remove(conversation_uuid, user_uuid):
            raise NotFoundError("Member not found")


class ActiveConnectionController(BaseController[ActiveConnection]):

    def __init__(self):
        super().__init__(
            repository=ActiveConnectionRepository(),
            event=None,
            cache=None
        )

    async def connect(self, conversation_uuid: str, user_uuid: str) -> ActiveConnection:
        return await self.repository.connect(conversation_uuid, user_uuid)

    async def disconnect(self, conversation_uuid: str, user_uuid: str) -> None:
        await self.repository.disconnect(conversation_uuid, user_uuid)



class MessageController(BaseController[Message]):

    def __init__(self):
        super().__init__(
            repository=MessageRepository(),
            event=None,
            cache=None
        )
