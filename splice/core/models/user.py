from typing import Optional, Dict, List, Any

from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema

from .linkusergroup import linkUserGroup

# import uuid
# from sqlmodel import SQLModel
from pydantic import ConfigDict

# Importe o modelo Establishment para evitar problemas de referência circular
from .establishment import Establishment
from .group import Group


class User(BaseTable, table=True):
    __tablename__ = 'users'

    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    phone: str = Field(index=True, unique=True, nullable=False)
    username: str = Field(index=True, unique=True, nullable=False)
    password: str = Field(nullable=False)
    photo: str = Field()

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


# Esquema para resposta que inclui relacionamentos serializados
class UserResponse(BaseTable):
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    photo: str
    establishment: Optional[Establishment] = None
    groups: Optional[List[Group]] = None
    # orders: Optional[List[Any]] = None

    model_config = ConfigDict(
        from_attributes=True,
    )

    # Método para converter para dicionário com relacionamentos
    # def model_dump(self, **kwargs):
    #     data = super().model_dump(**kwargs)
    #     if self.establishment:
    #         data["establishment"] = self.establishment.model_dump(**kwargs)
    #     if self.groups:
    #         data["groups"] = [
    #             group.model_dump(**kwargs) for group in self.groups
    #         ]
    #     if self.orders:
    #         data["orders"] = [
    #             order.model_dump(**kwargs) for order in self.orders
    #         ]
    #     return data
