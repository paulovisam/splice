from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.infra.database import get_db
from splice.infra.repositories.user_repository import UserRepository
from splice.interface.schemas.user_schema import (
    UserCreateSchema,
    UserResponseSchema,
)
from splice.interface.service.user_service import UserService

router = APIRouter()


@router.get('/usuarios/{user_id}', response_model=UserResponseSchema)
async def buscar_usuario(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = UserService(repo)
    usuario = service.buscar_usuario(user_id)
    if not usuario:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return usuario


@router.post('/usuarios', response_model=UserResponseSchema)
async def criar_usuario(
    data: UserCreateSchema = Body(),
    db: Session = Depends(get_db),
):
    repo = UserRepository(db)
    service = UserService(repo)
    usuario = await service.criar_usuario(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        email=data.email,
        username=data.username,
        password=data.password,
        photo=data.photo,
    )
    return usuario
