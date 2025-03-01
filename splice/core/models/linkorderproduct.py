import uuid

from splice.infra.database.base import Field, SQLModel


class linkOrderProduct(SQLModel, table=True):
    product_id: uuid.UUID = Field(
        default=None, foreign_key='products.id', primary_key=True
    )
    order_id: uuid.UUID = Field(
        default=None, foreign_key='orders.id', primary_key=True
    )

    # primary_key: garante que vou ter somente uma única combinação
    # de product e order
    # default none: permite criar orders sem product e vice-versa
