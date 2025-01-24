from splice.infra.repositories.message_repository import MessageRepository
from splice.interface.schemas.message_schema import MessageCreateSchema


class CreateMessage:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    async def execute(self, content: str, sender: str, receiver: str):
        new_message = MessageCreateSchema(
            content=content,
            sender=sender,
            receiver=receiver,
        )
        return await self.message_repository.save(new_message)
