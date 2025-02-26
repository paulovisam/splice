# app/api/schemas/order_schema.py
from uuid import UUID

from pydantic import BaseModel


class OrderCreateSchema(BaseModel):
    # TODO - #dados do modelo
    pass


class OrderUpdateSchema(BaseModel):
    id: str
    # TODO - colocar dados do modelo


class OrderResponseSchema(OrderCreateSchema):
    id: UUID

    class Config:
        from_attributes = True
