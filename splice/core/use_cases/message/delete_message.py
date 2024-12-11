from splice.infra.repositories.message_repository import MessageRepository


class DeleteMessage:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    async def execute(self, message_id: str):
        return await self.message_repository.delete(message_id=message_id)
