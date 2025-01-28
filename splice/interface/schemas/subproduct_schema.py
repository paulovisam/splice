# app/api/schemas/subproduct_schema.py
from pydantic import BaseModel


class SubproductCreateSchema(BaseModel):
    id_product: str
    name: str
    value: float
    amount: int
    description: str

class SubproductUpdateSchema(BaseModel):
    id: str
    id_product: str = None
    name: str = None
    value: float = None
    amount: int = None
    description: str = None

class SubproductResponseSchema(SubproductCreateSchema):
    id: str

    class Config:
        from_attributes = True
