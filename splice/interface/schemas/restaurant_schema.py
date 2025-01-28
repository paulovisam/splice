from pydantic import BaseModel
from uuid import UUID

class RestaurantCreateSchema(BaseModel):
    user_id: str
    name: str
    description: str
    photo: str

class RestaurantUpdateSchema(BaseModel):
    id: str
    user_id: str = None
    name: str = None
    description: str = None
    photo: str = None

class RestaurantRespondeSchema(RestaurantCreateSchema):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True