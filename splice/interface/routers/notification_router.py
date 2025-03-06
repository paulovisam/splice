from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from splice.infra.database import get_mongo_session, get_pg_session
from splice.infra.repositories.message_repository import MessageRepository
from splice.infra.repositories.notification_repository import (
    NotificationRepository,
)
from splice.infra.repositories.user_repository import UserRepository
from splice.interface.schemas.notification_schema import (
    NotificationCreateSchema,
    NotificationResponseSchema,
)
from splice.interface.service.notification_service import NotificationService

router = APIRouter(prefix='/notifications')


@router.post('', response_model=NotificationResponseSchema)
async def create(
    data: NotificationCreateSchema,
    mongo_db: Session = Depends(get_mongo_session),
    postgress_db: Session = Depends(get_pg_session),
):
    notification_repository = NotificationRepository(mongo_session=mongo_db)
    user_repositor = UserRepository(db_session=postgress_db)
    message_repository = MessageRepository(mongo_session=mongo_db)
    service = NotificationService(
        notification_repository=notification_repository,
        user_repository=user_repositor,
        message_repository=message_repository,
    )
    return await service.create_notification(
        message_id=data.message_id, user_id=data.user_id, is_read=data.is_read
    )


@router.get('', response_model=NotificationResponseSchema)
async def get(
    notification_id: str = None,
    mongo_db: Session = Depends(get_mongo_session),
    postgress_db: Session = Depends(get_pg_session),
):
    notification_repository = NotificationRepository(mongo_session=mongo_db)
    user_repositor = UserRepository(db_session=postgress_db)
    message_repository = MessageRepository(mongo_session=mongo_db)
    service = NotificationService(
        notification_repository=notification_repository,
        user_repository=user_repositor,
        message_repository=message_repository,
    )
    return await service.get_by_id(notification_id)


@router.delete('')
async def delete(
    notification_id: str = None,
    mongo_db: Session = Depends(get_mongo_session),
    postgress_db: Session = Depends(get_pg_session),
):
    notification_repository = NotificationRepository(mongo_session=mongo_db)
    user_repositor = UserRepository(db_session=postgress_db)
    message_repository = MessageRepository(mongo_session=mongo_db)
    service = NotificationService(
        notification_repository=notification_repository,
        user_repository=user_repositor,
        message_repository=message_repository,
    )
    return await service.delete_notification(notification_id)
