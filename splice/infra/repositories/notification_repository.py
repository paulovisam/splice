from typing import Optional

from bson import ObjectId
from fastapi.exceptions import HTTPException
from pymongo import errors
from pymongo.database import Database

from splice.interface.schemas.notification_schema import (
    NotificationCreateSchema,
    NotificationResponseSchema,
)


class NotificationRepository:
    def __init__(self, mongo_session: Database):
        self.collection = mongo_session.get_collection('notifications')

    async def save(
        self, data: NotificationCreateSchema
    ) -> NotificationResponseSchema:
        try:
            result = await self.collection.insert_one(data.model_dump())
            if result:
                return NotificationResponseSchema(
                    id=str(result.inserted_id),
                    is_read=data.is_read,
                    message_id=data.message_id,
                    user_id=data.user_id,
                )
        except (ValueError, TypeError) as e:
            raise e
        except errors.PyMongoError:
            raise HTTPException(
                status_code=500, detail='Error inserting notification'
            )

    async def get_by_id(
        self, notification_id: str
    ) -> Optional[NotificationResponseSchema]:
        notification = await self.collection.find_one({
            '_id': ObjectId(notification_id)
        })
        if notification:
            return NotificationResponseSchema(
                id=str(notification['_id']),
                message_id=str(notification['message_id']),
                user_id=str(notification['user_id']),
                is_read=notification['is_read'],
            )
        raise HTTPException(status_code=404, detail='Notification not found')

    async def delete(self, notification_id: str) -> None:
        try:
            if not notification_id:
                raise ValueError('Notification ID is required for delete.')
            await self.collection.delete_one({
                '_id': ObjectId(notification_id)
            })
        except (ValueError, TypeError) as e:
            raise e
        except errors.PyMongoError as e:
            raise HTTPException(
                status_code=400,
                detail=f'Erro ao excluir notificação com ID {notification_id}: {e}',  # noqa: E501
            )
