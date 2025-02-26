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
    CREDIT_CARD = 'CREDIT_CARD'
    DEBIT_CARD = 'DEBIT_CARD'
    PAYPAL = 'PAYPAL'
    BANK_TRANSFER = 'BANK_TRANSFER'
    CASH = 'CASH'
    CRYPTOCURRENCY = 'CRYPTOCURRENCY'
    APPLE_PAY = 'APPLE_PAY'
    GOOGLE_PAY = 'GOOGLE_PAY'
    PIX = 'PIX'


class Order(BaseTable, table=True):
    __tablename__ = 'orders'
    value: float = Field(nullable=False)
    payment_method: PaymentType = Field(
        sa_column=Column(SAEnum(PaymentType, name='paymeny_type_enum'))
    )
    has_paid: bool = Field(default=False)

    # Relação com a tabela 'users'
    user_id: uuid.UUID = Field(foreign_key='users.id')
    user: User = Relationship(
        back_populates='orders', sa_relationship_kwargs={'lazy': 'selectin'}
    )

    # Relação com a tabela 'users'
    establishment_id: uuid.UUID = Field(foreign_key='establishments.id')
    establishment: Establishment = Relationship(
        back_populates='orders', sa_relationship_kwargs={'lazy': 'selectin'}
    )


OrderCreateSchema = generate_schema(Order)
OrderUpdateSchema = generate_schema(Order, optional=True)
