from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.infra.database import get_session
from splice.infra.repositories.user_repository import UserRepository
from splice.interface.schemas.user_schema import (
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema,
)
from splice.interface.service.user_service import UserService

router = APIRouter(prefix='/users')


@router.get('', response_model=UserResponseSchema)
async def get_user(
    user_id: str = None,
    username: str = None,
    email: str = None,
    phone: str = None,
    db_session: Session = Depends(get_session),
):
    repo = UserRepository(db_session)
    service = UserService(repo)

    if user_id:
        usuario = await service.get_user(user_id)
    elif username:
        usuario = await service.get_user_by_username(username)
    elif email:
        usuario = await service.get_user_by_email(email)
    elif phone:
        usuario = await service.get_user_by_phone(phone)
    else:
        raise HTTPException(
            status_code=400, detail='Parâmetro de consulta necessário'
        )

    if not usuario:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')

    return usuario


@router.post('', response_model=UserResponseSchema)
async def create_user(
    data: UserCreateSchema = Body(),
    db_session: Session = Depends(get_session),
):
    repo = UserRepository(db_session)
    service = UserService(repo)
    usuario = await service.create_user(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        email=data.email,
        username=data.username,
        password=data.password,
        photo=data.photo,
    )
    return usuario


@router.put('', response_model=UserResponseSchema)
async def update_user(
    data: UserUpdateSchema = Body(), db_session: Session = Depends(get_session)
):
    repo = UserRepository(db_session)
    service = UserService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update_user(user_id=data.id, **update_data)


@router.delete('')
async def delete_user(user_id: str, db_session=Depends(get_session)):
    repo = UserRepository(db_session)
    service = UserService(repo)
    return await service.delete_user(user_id)
