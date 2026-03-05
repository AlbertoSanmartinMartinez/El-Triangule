import json
from collections import defaultdict

from fastapi import WebSocket, WebSocketDisconnect

from app.src.messages.models import Message
from app.src.messages.controller import MessageController, ActiveConnectionController

message_controller = MessageController()
connection_controller = ActiveConnectionController()

local_connections: dict[str, dict[str, WebSocket]] = defaultdict(dict)


async def conversation_websocket(websocket: WebSocket, conversation_uuid: str):
    await websocket.accept()

    user_uuid = websocket.query_params.get("user_uuid")
    if not user_uuid:
        await websocket.close(code=4001, reason="user_uuid required")
        return

    await connection_controller.connect(conversation_uuid, user_uuid)
    local_connections[conversation_uuid][user_uuid] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            action = payload.get("action", "message")

            if action == "message":
                message = Message(
                    conversation_uuid=conversation_uuid,
                    sender_uuid=user_uuid,
                    content=payload["content"],
                    created_by=user_uuid,
                )
                saved = await message_controller.create(message)

                broadcast = json.dumps({
                    "action": "message",
                    "uuid": str(saved.uuid),
                    "conversation_uuid": conversation_uuid,
                    "sender_uuid": user_uuid,
                    "content": saved.content,
                    "created_at": saved.created_at.isoformat() if saved.created_at else None,
                })
                for uid, conn in local_connections[conversation_uuid].items():
                    await conn.send_text(broadcast)

            elif action == "typing":
                broadcast = json.dumps({
                    "action": "typing",
                    "sender_uuid": user_uuid,
                })
                for uid, conn in local_connections[conversation_uuid].items():
                    if uid != user_uuid:
                        await conn.send_text(broadcast)

            elif action == "read":
                broadcast = json.dumps({
                    "action": "read",
                    "sender_uuid": user_uuid,
                    "last_read_message_uuid": payload.get("last_read_message_uuid"),
                })
                for uid, conn in local_connections[conversation_uuid].items():
                    if uid != user_uuid:
                        await conn.send_text(broadcast)

    except WebSocketDisconnect:
        local_connections[conversation_uuid].pop(user_uuid, None)
        if not local_connections[conversation_uuid]:
            del local_connections[conversation_uuid]
        await connection_controller.disconnect(conversation_uuid, user_uuid)
