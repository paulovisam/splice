from splice.infra.repositories.message_repository import MessageRepository


class GetMessage:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    async def get_by_id(self, message_id: str):
        return await self.message_repository.get_by_id(message_id=message_id)

    async def get_by_sender(self, sender_username: str):
        return await self.message_repository.get_by_sender_id(
            sender_username=sender_username
        )

    async def get_by_receiver(self, receiver_username: str):
        return await self.message_repository.get_by_receiver_id(
            receiver_username=receiver_username
        )
