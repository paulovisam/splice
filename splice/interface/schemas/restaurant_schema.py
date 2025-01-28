# app/api/schemas/restaurant_schema.py
from pydantic import BaseModel


class RestaurantCreateSchema(BaseModel):
    id_user: str
    description: str
    name: str
    category: str
    photo: str

class RestaurantUpdateSchema(BaseModel):
    id: str
    id_user: str = None
    description: str = None
    name: str = None
    category: str = None
    photo: str = None

class RestaurantResponseSchema(RestaurantCreateSchema):
    id: str

    class Config:
        from_attributes = True
