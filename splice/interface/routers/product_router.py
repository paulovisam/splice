from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.core.models.product import (
    Product,
    ProductCreateSchema,
    ProductUpdateSchema,
)
from splice.core.models.user import User
from splice.infra.database import get_pg_session
from splice.infra.repositories.product_repository import ProductRepository
from splice.interface.service.auth_service import get_current_user
from splice.interface.service.product_service import ProductService

router = APIRouter(prefix='/products')


@router.get('', response_model=Product)
async def get(
    product_id: str = None,
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = ProductRepository(db_session)
    service = ProductService(repo)

    if product_id:
        product = await service.get_by_id(product_id)
    else:
        raise HTTPException(
            status_code=400, detail='Parâmetro de consulta necessário'
        )

    if not product:
        raise HTTPException(status_code=404, detail='Product não encontrado')

    return product


@router.post('', response_model=Product)
async def create(
    data: ProductCreateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = ProductRepository(db_session)
    service = ProductService(repo)
    product = await service.create(**data.model_dump())
    return product


@router.put('', response_model=Product)
async def update(
    data: ProductUpdateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = ProductRepository(db_session)
    service = ProductService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update(product_id=data.id, **update_data)


@router.delete('')
async def delete(
    product_id: str,
    db_session=Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = ProductRepository(db_session)
    service = ProductService(repo)
    return await service.delete(product_id)
