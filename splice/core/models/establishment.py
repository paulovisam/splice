import uuid
from typing import Optional

from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema

from .user import User


class Establishment(BaseTable, table=True):
    __tablename__ = "establishments"

    name: str = Field(nullable=False)
    description: str
    photo: str

    # Relação com a tabela 'users'
    user_id: uuid.UUID = Field(foreign_key="users.id")
    user: User = Relationship(
        back_populates="establishment", sa_relationship_kwargs={"lazy": "selectin"}
    )

    orders: Optional["Order"] = Relationship(
        back_populates="establishment", sa_relationship_kwargs={"lazy": "selectin"}
    )
    # Serializar Relacionamentos
    # class Config:
    #     from_attributes = True


# class establishmentResponse(establishment):
#     user: User


EstablishmentCreateSchema = generate_schema(Establishment)
EstablishmentUpdateSchema = generate_schema(Establishment, optional=True)
