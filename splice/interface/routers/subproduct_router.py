from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.core.models.subproduct import (
    Subproduct,
    SubproductCreateSchema,
    SubproductUpdateSchema,
)
from splice.core.models.user import User
from splice.infra.database import get_pg_session
from splice.infra.repositories.subproduct_repository import (
    SubproductRepository,
)
from splice.interface.service.auth_service import get_current_user
from splice.interface.service.subproduct_service import SubproductService

router = APIRouter(prefix='/subproducts')
# TODO: adicionar router em app.py


@router.get('', response_model=Subproduct)
async def get(
    subproduct_id: str = None,
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = SubproductRepository(db_session)
    service = SubproductService(repo)

    if subproduct_id:
        subproduct = await service.get_by_id(subproduct_id)
    else:
        raise HTTPException(
            status_code=400, detail='Parâmetro de consulta necessário'
        )

    if not subproduct:
        raise HTTPException(
            status_code=404, detail='Subproduct não encontrado'
        )

    return subproduct


@router.post('', response_model=Subproduct)
async def create(
    data: SubproductCreateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = SubproductRepository(db_session)
    service = SubproductService(repo)
    subproduct = await service.create(**data.model_dump())
    return subproduct


@router.put('', response_model=Subproduct)
async def update(
    data: SubproductUpdateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = SubproductRepository(db_session)
    service = SubproductService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update(subproduct_id=data.id, **update_data)


@router.delete('')
async def delete(
    subproduct_id: str,
    db_session=Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = SubproductRepository(db_session)
    service = SubproductService(repo)
    return await service.delete(subproduct_id)
