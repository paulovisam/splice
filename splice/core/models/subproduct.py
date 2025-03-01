import uuid

from sqlmodel import Relationship

from splice.infra.database.base import BaseTable, Field
from splice.utils.generate_schemas import generate_schema


class Subproduct(BaseTable, table=True):
    __tablename__ = 'subproducts'
    name: str = Field(nullable=False)
    value: float = Field(nullable=False)
    description: str

    product_id: uuid.UUID = Field(foreign_key='products.id')
    product: 'Product' = Relationship(  # type: ignore #noqa: F821
        back_populates='subproducts',
        sa_relationship_kwargs={'lazy': 'selectin'},
    )


SubproductCreateSchema = generate_schema(Subproduct)
SubproductUpdateSchema = generate_schema(Subproduct, optional=True)
