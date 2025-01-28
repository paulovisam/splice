from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from splice.infra.database import get_session
from splice.infra.repositories.restaurant_repository import RestaurantRepository
from splice.interface.schemas.restaurant_schema import RestaurantCreateSchema, RestaurantRespondeSchema, RestaurantUpdateSchema
from splice.interface.service.restaurant_service import RestaurantService

router = APIRouter(prefix='/restaurant')

@router.post('')
async def create_restaurant(
    data: RestaurantCreateSchema,
    db: Session = Depends(get_session)
):
    repo = RestaurantRepository(db)
    service = RestaurantService(repo)
    print(data.model_dump())
    print(type(data.model_dump()))
    return await service.create_restaurant(**data.model_dump())

@router.get('', response_model=RestaurantRespondeSchema)
async def get_restaurant(
    restaurant_id: str = None,
    user_id: str = None,
    db: Session = Depends(get_session)
):
    repo = RestaurantRepository(db)
    service = RestaurantService(repo)
    return await service.get_restaurant(restaurant_id=restaurant_id, user_id=user_id)

@router.put('')
async def update_restaurant(
    data: RestaurantUpdateSchema,
    db: Session = Depends(get_session)
):
    repo = RestaurantRepository(db)
    service = RestaurantService(repo)
    return await service.update_restaurant(**data.model_dump())

@router.delete('')
async def delete_restaurant(
    restaurant_id: str,
    db: Session = Depends(get_session)
):
    repo = RestaurantRepository(db)
    service = RestaurantService(repo)
    return await service.delete_restaurant(restaurant_id=restaurant_id)
