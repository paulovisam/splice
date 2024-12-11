from fastapi import WebSocket, WebSocketDisconnect


class WSService:
    def __init__(self):
        PORTS = [8080]
        self.clients = {port: {} for port in PORTS}

    async def handle_client(
        self, websocket: WebSocket, port: int, chat_id: str
    ):
        await websocket.accept()
        if chat_id not in self.clients[port]:
            self.clients[port][chat_id] = set()
        self.clients[port][chat_id].add(websocket)

        print(
            f'Conexão estabelecida com {websocket.client}, chat_id: {chat_id}'
        )

        try:
            while True:
                message = (
                    await websocket.receive_text()
                )  # Recebe uma mensagem de texto
                print(
                    f'Mensagem recebida de {websocket.client} na porta {port}, chat_id: {chat_id}: {message}'
                )

                # Enviar para todos os clientes conectados, exceto o remetente
                for client in self.clients[port][chat_id]:
                    if client != websocket:
                        await client.send_text(message)
        except WebSocketDisconnect:
            self.clients[port][chat_id].remove(websocket)
            print(
                f'Cliente {websocket.client} desconectado na porta {port}, chat_id: {chat_id}'
            )
