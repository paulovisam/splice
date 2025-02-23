from uuid import UUID

from pydantic import BaseModel


class establishmentCreateSchema(BaseModel):
    user_id: str
    name: str
    description: str
    photo: str


class establishmentUpdateSchema(BaseModel):
    id: str
    user_id: str = None
    name: str = None
    description: str = None
    photo: str = None


class establishmentResponseSchema(establishmentCreateSchema):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True
