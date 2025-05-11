from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.core.models.user import (
    User,
    UserCreateSchema,
    UserResponse,
    UserUpdateSchema,
)
from splice.infra.database import get_pg_session
from splice.infra.repositories.user_repository import UserRepository
from splice.interface.exceptions.custom_exceptions import AcessoNegado
from splice.interface.service.auth_service import get_current_user
from splice.interface.service.user_service import UserService


router = APIRouter(prefix='/users')


@router.get('', response_model=UserResponse)
async def get(
    user_id: str = None,
    username: str = None,
    email: str = None,
    phone: str = None,
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = UserRepository(db_session)
    service = UserService(repo)

    if user_id:
        if user_id != str(current_user.id):
            raise AcessoNegado()
        usuario = await service.get_user_by_id(user_id)
    elif username:
        if username != current_user.username:
            raise AcessoNegado()
        usuario = await service.get_user_by_username(username)
    elif email:
        if email != current_user.email:
            raise AcessoNegado()
        usuario = await service.get_user_by_email(email)
    elif phone:
        if phone != current_user.phone:
            raise AcessoNegado()
        usuario = await service.get_user_by_phone(phone)
    else:
        raise HTTPException(
            status_code=400, detail='Parâmetro de consulta necessário'
        )

    if not usuario:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return usuario


@router.post('', response_model=UserResponse)
async def create(
    data: UserCreateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
):
    repo = UserRepository(db_session)
    service = UserService(repo)
    usuario = await service.create_user(**data.model_dump())
    return usuario


@router.put('', response_model=UserResponse)
async def update(
    data: UserUpdateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = UserRepository(db_session)
    service = UserService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)
    if data.id != current_user.id:
        raise AcessoNegado()
    # Passa os dados descompactados para a função de atualização
    return await service.update_user(user_id=data.id, **update_data)


@router.delete('')
async def delete(
    user_id: str,
    db_session=Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = UserRepository(db_session)
    service = UserService(repo)
    if user_id != str(current_user.id):
        raise AcessoNegado()
    return await service.delete_user(user_id)
