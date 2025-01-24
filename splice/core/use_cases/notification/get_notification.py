from splice.infra.repositories.notification_repository import (
    NotificationRepository,
)


class GetNotification:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    async def execute(self, notificaion_id: str):
        return await self.notification_repository.get_by_id(notification_id=notificaion_id)
