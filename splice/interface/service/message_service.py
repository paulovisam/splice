from splice.core.use_cases.message.create_message import CreateMessage
from splice.core.use_cases.message.delete_message import DeleteMessage
from splice.core.use_cases.message.get_message import GetMessage
from splice.infra.repositories.message_repository import MessageRepository


class MessageService:
    def __init__(self, repo: MessageRepository):
        self.repo = repo

    async def create_message(self, content: str, sender: str, receiver: str):
        use_case = CreateMessage(self.repo)
        return await use_case.execute(
            content=content, sender=sender, receiver=receiver
        )

    async def get_message(self, message_id: str):
        use_case = GetMessage(self.repo)
        return await use_case.get_by_id(message_id=message_id)

    async def delete_message(self, message_id: str):
        use_case = DeleteMessage(self.repo)
        return await use_case.execute(message_id=message_id)
