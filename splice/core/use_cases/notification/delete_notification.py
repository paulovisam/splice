from splice.infra.repositories.notification_repository import (
    NotificationRepository,
)


class DeleteNotification:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    async def execute(self, notification_id: str):
        return await self.notification_repository.delete(notification_id=notification_id)
