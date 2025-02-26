import enum
import uuid

from sqlalchemy import Column
from sqlalchemy import Enum as SAEnum
from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema

from .establishment import Establishment
from .user import User


class PaymentType(enum.Enum):
    money = "money"
    pix = "pix"
    card = "card"


class Order(BaseTable, table=True):
    __tablename__ = 'orders'
    # TODO - preencher os dados
    value: float = Field(nullable=False)
    payment_method: PaymentType = Field(
        sa_column=Column(SAEnum(PaymentType, name="paymeny_type_enum"))
    )
    has_paid: bool = Field(default=False)

    # Relação com a tabela 'users'
    user_id: uuid.UUID = Field(foreign_key="users.id")
    user: User = Relationship(
        back_populates="orders", sa_relationship_kwargs={"lazy": "selectin"}
    )

    # Relação com a tabela 'users'
    establishment_id: uuid.UUID = Field(foreign_key="establishments.id")
    establishment: Establishment = Relationship(
        back_populates="orders", sa_relationship_kwargs={"lazy": "selectin"}
    )


OrderCreateSchema = generate_schema(Order)
OrderUpdateSchema = generate_schema(Order, optional=True)
