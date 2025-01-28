from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from splice.infra.database import get_session
from splice.infra.repositories.restaurant_repository import RestaurantRepository
from splice.interface.schemas.restaurant_schema import (
    RestaurantCreateSchema,
    RestaurantResponseSchema,
    RestaurantUpdateSchema,
)
from splice.interface.service.restaurant_service import RestaurantService

router = APIRouter(prefix='/restaurants')


@router.get('')
async def get(
    restaurant_id: str = None,
    db_session: Session = Depends(get_session),
):
    repo = RestaurantRepository(db_session)
    service = RestaurantService(repo)

    if restaurant_id:
        restaurant = await service.get_by_id(restaurant_id)
    else:
        raise HTTPException(
            status_code=400, detail='Parâmetro de consulta necessário'
        )

    if not restaurant:
        raise HTTPException(status_code=404, detail='Restaurant não encontrado')

    return restaurant


@router.post('', response_model=RestaurantResponseSchema)
async def create(
    data: RestaurantCreateSchema = Body(),
    db_session: Session = Depends(get_session),
):
    repo = RestaurantRepository(db_session)
    service = RestaurantService(repo)
    restaurant = await service.create(
        id_user=data.id_user,
        description=data.description,
        name=data.name,
        category=data.category,
        photo=data.photo,
    )
    return restaurant


@router.put('', response_model=RestaurantResponseSchema)
async def update(
    data: RestaurantUpdateSchema = Body(), db_session: Session = Depends(get_session)
):
    repo = RestaurantRepository(db_session)
    service = RestaurantService(repo)

    # Converte o body em dicionário, removendo campos nulos
    update_data = data.model_dump(exclude_unset=True)

    # Passa os dados descompactados para a função de atualização
    return await service.update(restaurant_id=data.id, **update_data)


@router.delete('')
async def delete(restaurant_id: str, db_session=Depends(get_session)):
    repo = RestaurantRepository(db_session)
    service = RestaurantService(repo)
    return await service.delete(restaurant_id)
