from splice.core.use_cases.notification.delete_notification import (
    DeleteNotification,
)
from splice.core.use_cases.notification.get_notification import GetNotification
from splice.core.use_cases.notification.save_notification import (
    SaveNotification,
)
from splice.infra.repositories.message_repository import MessageRepository
from splice.infra.repositories.notification_repository import (
    NotificationRepository,
)
from splice.infra.repositories.user_repository import UserRepository
from splice.interface.exceptions.custom_exceptions import NotFoundException


class NotificationService:
    def __init__(
        self,
        notification_repository: NotificationRepository,
        user_repository: UserRepository,
        message_repository: MessageRepository,
    ):
        self.notification_repository = notification_repository
        self.user_repository = user_repository
        self.message_repository = message_repository

    async def create_notification(
        self, message_id: str, user_id: str, is_read: bool
    ):
        if await self.user_repository.get_by_id(user_id) is None:
            raise NotFoundException(detail='User not found')
        if await self.message_repository.get_by_id(message_id) is None:
            raise NotFoundException(detail='Message not found')
        use_case = SaveNotification(self.notification_repository)
        return await use_case.execute(
            message_id=message_id, user_id=user_id, is_read=is_read
        )

    async def get_by_id(self, notification_id: str):
        use_case = GetNotification(self.notification_repository)
        return await use_case.execute(notificaion_id=notification_id)

    async def delete_notification(self, notification_id: str):
        use_case = DeleteNotification(self.notification_repository)
        return await use_case.execute(notification_id=notification_id)
