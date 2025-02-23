import uuid

from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema

from .user import User


class Restaurant(BaseTable, table=True):
    __tablename__ = "restaurants"

    name: str = Field(nullable=False)
    description: str
    photo: str

    # Relação com a tabela 'users'
    user_id: uuid.UUID = Field(foreign_key="users.id")
    user: User = Relationship(
        back_populates="restaurant", sa_relationship_kwargs={"lazy": "selectin"}
    )

    # Serializar Relacionamentos
    # class Config:
    #     from_attributes = True


# class RestaurantResponse(Restaurant):
#     user: User


RestaurantCreateSchema = generate_schema(Restaurant)
RestaurantUpdateSchema = generate_schema(Restaurant, optional=True)
