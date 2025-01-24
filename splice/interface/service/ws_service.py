from fastapi import WebSocket, WebSocketDisconnect

from splice.infra.repositories.redis_repository import RedisRepository

global clients
clients = {}


class WSService:
    def __init__(self):
        self.clients = clients
        self.redis = RedisRepository()

    async def handle_client(
        self, websocket: WebSocket, chat_id: str
    ):

        await websocket.accept()
        if chat_id not in self.clients:
            self.clients[chat_id] = set()
        self.clients[chat_id].add(websocket)
        # self.redis.add_client_ws(chat_id=chat_id, websocket=websocket)

        print(f'Conexão estabelecida com {websocket.client}, chat_id: {chat_id}')
        print(self.clients[chat_id])
        print(len(self.clients[chat_id]))

        try:
            while True:
                message = await websocket.receive_text()
                print(
                    f'Mensagem recebida de {websocket.client}, chat_id: {chat_id}: {message}'
                )

                # for client in self.clients[chat_id]:
                for client in self.redis.get_clients_ws(chat_id=chat_id):
                    if client != websocket:
                        await client.send_text(message)
        except WebSocketDisconnect:
            # self.clients[chat_id].remove(websocket)
            self.redis.remove_client_ws(chat_id=chat_id)
            if not self.clients[chat_id]:
                del self.clients[chat_id]
            print(f'Cliente {websocket.client} desconectado, chat_id: {chat_id}')
