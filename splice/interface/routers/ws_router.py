from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from splice.interface.service.ws_service import WSService

router = APIRouter()


@router.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f'Message text was: {data}')
    except WebSocketDisconnect:
        await websocket.close()


@router.websocket('/ws/{chat_id}')
async def websocket_endpoint_chat_id(websocket: WebSocket, chat_id: str):
    service = WSService()

    if chat_id is None:
        await websocket.close(
            code=4000, reason='chat_id não fornecido na query'
        )
        return
    await service.handle_client(websocket, chat_id)
