import uuid
from typing import Optional

from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema

from .establishment import Establishment
from .linkorderproduct import linkOrderProduct


class Product(BaseTable, table=True):
    __tablename__ = 'products'
    name: str = Field(nullable=False)
    value: float = Field(nullable=False)
    description: str

    # Relação com a tabela 'establishment'
    establishment_id: uuid.UUID = Field(foreign_key='establishments.id')
    establishment: Establishment = Relationship(
        back_populates='products', sa_relationship_kwargs={'lazy': 'selectin'}
    )

    # Relação com a tabela 'orders'
    orders: Optional[list['Order']] = Relationship(  # type: ignore #noqa: F821
        back_populates='products',
        link_model=linkOrderProduct,
        sa_relationship_kwargs={'lazy': 'selectin'},
    )


ProductCreateSchema = generate_schema(Product)
ProductUpdateSchema = generate_schema(Product, optional=True)
