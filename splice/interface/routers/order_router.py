from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import Union, List

from splice.infra.database import get_pg_session
from splice.infra.repositories.order_repository import OrderRepository
from splice.core.models.order import OrderCreateSchema, OrderUpdateSchema, Order
from splice.interface.service.order_service import OrderService

router = APIRouter(prefix='/orders')


@router.get('', response_model=List[Order])
async def get_order(
    order_id: str = None,
    user_id: str = None,
    establishment_id: str = None,
    db_session: Session = Depends(get_pg_session),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)

    if order_id:
        order = [await service.get_by_id(order_id)]
    elif user_id:
        order = await service.get_by_user_id(user_id)
    elif establishment_id:
        order = await service.get_by_establishment_id(establishment_id)
    else:
        raise HTTPException(status_code=400, detail='Parâmetro de consulta necessário')

    if not order:
        raise HTTPException(status_code=404, detail='Order não encontrado')

    return order


@router.post('', response_model=Order)
async def create_order(
    data: OrderCreateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)
    order = await service.create(**data.model_dump())
    return order


@router.put('', response_model=Order)
async def update_order(
    data: OrderUpdateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update(order_id=data.id, **update_data)


@router.delete('')
async def delete_order(order_id: str, db_session=Depends(get_pg_session)):
    repo = OrderRepository(db_session)
    service = OrderService(repo)
    return await service.delete(order_id)
