from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from splice.infra.database import get_mongo_session
from splice.infra.repositories.message_repository import MessageRepository
from splice.interface.schemas.message_schema import (
    MessageCreateSchema,
    MessageResponseSchema,
)
from splice.interface.service.message_service import MessageService

router = APIRouter(prefix='/message')


@router.post('', response_model=MessageResponseSchema)
async def create_message(
    data: MessageCreateSchema, db: Session = Depends(get_mongo_session)
):
    repo = MessageRepository(db)
    service = MessageService(repo)
    return await service.create_message(
        content=data.content,
        sender=data.sender,
        receiver=data.receiver,
    )


@router.get('/{username}', response_model=List[MessageResponseSchema])
async def get_messages_by_username(
    username: str, db=Depends(get_mongo_session)
):
    repo = MessageRepository(db)
    service = MessageService(repo)
    return await service.get_messages_by_username(username)
