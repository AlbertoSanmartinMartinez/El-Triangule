from fastapi import Request, HTTPException, WebSocket, status

from app.src.base.router import BaseRouter
from app.src.base.error import AppError
from app.src.config import settings
from app.src.messages.models import Conversation, ConversationMember, Message, AddMemberRequest
from app.src.messages.controller import ConversationController, MessageController
from app.src.messages.websocket import conversation_websocket

conversation_router: BaseRouter[Conversation] = BaseRouter(
    model=Conversation,
    controller=ConversationController,
    prefix=f"/{settings.api_prefix}/messages/conversation",
    tags=["Conversation"],
)


@conversation_router.router.post(
    "/{uuid}/member",
    response_model=ConversationMember,
    status_code=status.HTTP_201_CREATED,
    summary="Add member to conversation",
)
async def add_member(uuid: str, request: Request, body: AddMemberRequest) -> ConversationMember:
    try:
        return await conversation_router.controller.add_member(uuid, body.user_uuid, request.state.user_uuid)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@conversation_router.router.delete(
    "/{uuid}/member/{user_uuid}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove member from conversation",
)
async def remove_member(uuid: str, user_uuid: str):
    try:
        await conversation_router.controller.remove_member(uuid, user_uuid)
    except AppError as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

message_router: BaseRouter[Message] = BaseRouter(
    model=Message,
    controller=MessageController,
    prefix=f"/{settings.api_prefix}/messages/message",
    tags=["Message"],
)

@conversation_router.router.websocket("/ws/conversation/{conversation_uuid}")
async def websocket_conversation(websocket: WebSocket, conversation_uuid: str):
    await conversation_websocket(websocket, conversation_uuid)
