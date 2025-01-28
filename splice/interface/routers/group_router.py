from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.infra.database import get_pg_session
from splice.infra.repositories.group_repository import GroupRepository
from splice.interface.schemas.group_schema import (
    GroupCreateSchema,
    GroupResponseSchema,
    GroupUpdateSchema,
)
from splice.interface.service.group_service import GroupService

router = APIRouter(prefix='/groups')


@router.get('', response_model=GroupResponseSchema)
async def get_group(
    group_id: str = None,
    db_session: Session = Depends(get_pg_session)
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


@router.post('', response_model=GroupResponseSchema)
async def post_group(
    data: GroupCreateSchema = Body(),
    db_session: Session = Depends(get_pg_session),
):
    repo = GroupRepository(db_session)
    service = GroupService(repo)
    group = await service.save_group(
        name=data.name,
        photo=data.photo,
    )
    return group


@router.put('', response_model=GroupResponseSchema)
async def update_group(
    data: GroupUpdateSchema = Body(),
    db_session: Session = Depends(get_pg_session)
):
    repo = GroupRepository(db_session)
    service = GroupService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update_group(group_id=data.id, **update_data)


@router.delete('')
async def delete_group(group_id: str, db_session=Depends(get_pg_session)):
    repo = GroupRepository(db_session)
    service = GroupService(repo)
    return await service.delete_group(group_id)
