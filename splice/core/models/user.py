from typing import Optional

from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema

from .linkusergroup import linkUserGroup

# import uuid
# from sqlmodel import SQLModel
# from pydantic import ConfigDict


class User(BaseTable, table=True):
    __tablename__ = 'users'

    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    phone: str = Field(index=True, unique=True, nullable=False)
    username: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    photo: str = Field()

    # TODO: retornar obj de establishment serializado na resposta
    establishment: Optional['Establishment'] = Relationship(  # type: ignore #noqa: F821
        back_populates='user', sa_relationship_kwargs={'lazy': 'selectin'}
    )

    groups: Optional[list['Group']] = Relationship(  # type: ignore #noqa: F821
        back_populates='users',
        link_model=linkUserGroup,
        sa_relationship_kwargs={'lazy': 'selectin'},
    )

    orders: Optional['Order'] = Relationship(  # type: ignore #noqa: F821
        back_populates='user', sa_relationship_kwargs={'lazy': 'selectin'}
    )


UserCreateSchema = generate_schema(User)
UserUpdateSchema = generate_schema(User, optional=True)

# class UserResponse(User):
#     establishment: dict
# model_config = ConfigDict(from_attributes=True)


#     # Serializar Relacionamentos
#     class Config:
#         from_attributes = True


# Gerando os schemas dinamicamente

# print(UserUpdateSchema.model_fields)
# print(UserUpdateSchema(id="", email="email.com"))

# establishment: Optional["establishment"]  = Relationship(
#     back_populates="user",
#     sa_relationship_kwargs={"lazy": "selectin"}
# )
# groups: Optional[list["Group"]] = Relationship(
#     back_populates="users",
#     link_model=linkUserGroup,
#     sa_relationship_kwargs={"lazy": "selectin"}
# )
