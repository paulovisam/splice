from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.core.models.group import (
    Group,
    GroupCreateSchema,
    GroupUpdateSchema,
)
from splice.core.models.user import User
from splice.infra.database import get_pg_session
from splice.infra.repositories.group_repository import GroupRepository
from splice.interface.service.auth_service import get_current_user
from splice.interface.service.group_service import GroupService

router = APIRouter(prefix='/groups')


@router.get('', response_model=Group)
async def get(
    group_id: str = None,
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = GroupRepository(db_session)
    service = GroupService(repo)

    if group_id:
        group = await service.get_by_id(group_id)
    else:
        raise HTTPException(
            status_code=400, detail='Parâmetro de consulta necessário'
        )

    if not group:
        raise HTTPException(status_code=404, detail='Grupo não encontrado')

    return group


@router.post('', response_model=Group)
async def post(
    data: GroupCreateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = GroupRepository(db_session)
    service = GroupService(repo)
    group = await service.save_group(
        name=data.name,
        photo=data.photo,
    )
    return group


@router.put('', response_model=Group)
async def update(
    data: GroupUpdateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = GroupRepository(db_session)
    service = GroupService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update_group(group_id=data.id, **update_data)


@router.delete('')
async def delete(
    group_id: str,
    db_session=Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = GroupRepository(db_session)
    service = GroupService(repo)
    return await service.delete_group(group_id)
