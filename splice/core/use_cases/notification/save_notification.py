from splice.infra.repositories.notification_repository import (
    NotificationRepository,
)
from splice.interface.schemas.notification_schema import (
    NotificationCreateSchema,
)


class SaveNotification:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    async def execute(self, message_id: str, user_id: str, is_read: bool):
        new_notification = NotificationCreateSchema(
            message_id=message_id,
            user_id=user_id,
            is_read=is_read,
        )
        return await self.notification_repository.save(new_notification)
