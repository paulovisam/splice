from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from splice.core.models.establishment import (
    establishment,
    establishmentCreateSchema,
    establishmentUpdateSchema,
)
from splice.infra.database import get_pg_session
from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)
from splice.interface.service.establishment_service import establishmentService

router = APIRouter(prefix="/establishment")


@router.post("", response_model=establishment)
async def create_establishment(
    data: establishmentCreateSchema,  # type: ignore
    db: Session = Depends(get_pg_session),
):
    repo = establishmentRepository(db)
    service = establishmentService(repo)
    print(data.model_dump())
    print(type(data.model_dump()))
    return await service.create_establishment(**data.model_dump())


@router.get("", response_model=establishment)
async def get_establishment(
    establishment_id: str = None,
    user_id: str = None,
    db: Session = Depends(get_pg_session),
):
    repo = establishmentRepository(db)
    service = establishmentService(repo)
    if establishment_id:
        establishment = await service.get_establishment_by_id(establishment_id=establishment_id)
    elif user_id:
        establishment = await service.get_establishment_by_user_id(user_id=user_id)
    else:
        raise HTTPException(status_code=400, detail="Query parameter required")
    if not establishment:
        raise HTTPException(status_code=404, detail="establishment not found")
    return establishment


@router.put("")
async def update_establishment(
    data: establishmentUpdateSchema, db: Session = Depends(get_pg_session)  # type: ignore
):
    repo = establishmentRepository(db)
    service = establishmentService(repo)
    return await service.update_establishment(**data.model_dump())


@router.delete("")
async def delete_establishment(establishment_id: str, db: Session = Depends(get_pg_session)):
    repo = establishmentRepository(db)
    service = establishmentService(repo)
    return await service.delete_establishment(establishment_id=establishment_id)
