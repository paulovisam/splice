from fastapi import WebSocket, WebSocketDisconnect

from splice.infra.repositories.redis_repository import RedisRepository
from splice.interface.service.message_service import MessageService

global clients
clients = {}


class WSService:
    def __init__(self, message_service: MessageService):
        self.clients = clients
        self.redis = RedisRepository()
        self.msg_service = message_service

    async def _send_text(self, client, message: str, sender: str, receiver: str):
        await client.send_text(message)
        await self.msg_service.create_message(
        content=message,
        sender=sender,
        receiver=receiver,
    )

    async def handle_client(
        self, websocket: WebSocket, user_id: str, chat_id: str
    ):

        await websocket.accept()
        if chat_id not in self.clients:
            self.clients[chat_id] = set()
        self.clients[chat_id].add((websocket, user_id))
        self.redis.add_client_ws(chat_id, websocket, user_id)

        print(f'Conexão estabelecida com {user_id}, chat_id: {chat_id}')
        print(self.clients[chat_id])
        print(len(self.clients[chat_id]))

        try:
            while True:
                message = await websocket.receive_text()
                print(
                    f'Mensagem recebida de {user_id}, chat_id: {chat_id}: {message}'
                )

                # for client, user_id in self.clients[chat_id]:
                for client_ws, user_id in self.redis.get_clients_ws(chat_id=chat_id):
                    if client_ws != websocket:
                        await self._send_text(message=message, sender=user_id, receiver=chat_id)
        except WebSocketDisconnect:
            # self.clients[chat_id].remove(websocket)
            self.redis.remove_client_ws(chat_id=chat_id)
            if not self.clients[chat_id]:
                del self.clients[chat_id]
            print(f'Cliente {websocket.client} desconectado, chat_id: {chat_id}')

# ? Dado que o servidor terá varias instâncias onde guardar os objetos websocket (do tipo WebSocket) que representam a conexão do cliente?

# Em um backend de um grande aplicativo de mensagens escalável com várias instâncias de backend, que usa protocolo websocket. Como é feito no código o gerenciamento de mensagens para grupos e usuários? Use python e fastapi websocket
