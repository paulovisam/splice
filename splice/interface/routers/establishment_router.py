from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from splice.core.models.establishment import (
    Establishment,
    EstablishmentCreateSchema,
    EstablishmentUpdateSchema,
)
from splice.core.models.user import User
from splice.infra.database import get_pg_session
from splice.infra.repositories.establishment_repository import (
    EstablishmentRepository,
)
from splice.interface.service.auth_service import get_current_user
from splice.interface.service.establishment_service import EstablishmentService

router = APIRouter(prefix='/establishments')


@router.post('', response_model=Establishment)
async def create(
    data: EstablishmentCreateSchema,  # type: ignore
    db: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = EstablishmentRepository(db)
    service = EstablishmentService(repo)
    print(data.model_dump())
    print(type(data.model_dump()))
    return await service.create_establishment(**data.model_dump())


@router.get('', response_model=Establishment)
async def get(
    establishment_id: str = None,
    user_id: str = None,
    db: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = EstablishmentRepository(db)
    service = EstablishmentService(repo)
    if establishment_id:
        establishment = await service.get_establishment_by_id(
            establishment_id=establishment_id
        )
    elif user_id:
        establishment = await service.get_establishment_by_user_id(
            user_id=user_id
        )
    else:
        raise HTTPException(status_code=400, detail='Query parameter required')
    if not establishment:
        raise HTTPException(status_code=404, detail='establishment not found')
    return establishment


@router.put('')
async def update(
    data: EstablishmentUpdateSchema,  # type: ignore
    db: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = EstablishmentRepository(db)
    service = EstablishmentService(repo)
    return await service.update_establishment(**data.model_dump())


@router.delete('')
async def delete(
    establishment_id: str,
    db: Session = Depends(get_pg_session),
    current_user: User = Depends(get_current_user),
):
    repo = EstablishmentRepository(db)
    service = EstablishmentService(repo)
    return await service.delete_establishment(
        establishment_id=establishment_id
    )
