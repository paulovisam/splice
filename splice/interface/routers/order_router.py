from typing import List, Dict, Any

from fastapi import APIRouter, Body, Depends, Response
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.core.models.order import (
    Order,
    OrderCreateSchema,
    OrderUpdateSchema,
)
from splice.core.models.user import User
from splice.infra.database import get_pg_session
from splice.infra.repositories.order_repository import OrderRepository
from splice.interface.service.auth_service import get_current_user
from splice.interface.service.order_service import OrderService

router = APIRouter(prefix='/orders')


@router.get('', response_model=Dict[str, Any])
async def get(
    response: Response,
    order_id: str = None,
    establishment_id: str = None,
    offset: int = 0,
    limit: int = 10,
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)

    if order_id:
        order = [await service.get_by_id(order_id)]
    elif establishment_id:
        order = await service.get_by_establishment_id(
            establishment_id, offset, limit
        )
        # Obtendo o total de pedidos para a paginação
        total_orders = await service.count_orders_establishment_id(
            establishment_id
        )
    else:
        order = await service.get_by_user_id(current_user.id, offset, limit)
        # Obtendo o total de pedidos para a paginação
        total_orders = await service.count_orders_user_id(current_user.id)

    if not order:
        raise HTTPException(status_code=404, detail='Order não encontrado')

    # Verificando se há próxima página
    has_next_page = offset + len(order) < total_orders

    # Definindo o cabeçalho Content-Range
    response.headers['Content-Range'] = (
        f'orders {offset}-{offset + len(order) - 1}/{total_orders}'
    )
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'

    return {
        "data": order,
        "total": total_orders,
        "pageInfo": {
            "hasNextPage": has_next_page,
            "hasPreviousPage": offset > 0,
        },
        "meta": {},  # Adicione metadados se necessário
    }


@router.post('', response_model=Order)
async def create(
    data: OrderCreateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)
    order = await service.create(**data.model_dump())
    return order


@router.put('', response_model=Order)
async def update(
    data: OrderUpdateSchema = Body(),  # type: ignore
    db_session: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update(order_id=data.id, **update_data)


@router.delete('')
async def delete(
    order_id: str,
    db_session=Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = OrderRepository(db_session)
    service = OrderService(repo)
    return await service.delete(order_id)
