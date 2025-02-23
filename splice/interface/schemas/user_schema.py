# app/api/schemas/user_schema.py
from uuid import UUID

from pydantic import BaseModel

from .establishment_schema import establishmentResponseSchema


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    phone: str
    email: str
    password: str
    photo: str


class UserUpdateSchema(BaseModel):
    id: str
    first_name: str = None
    last_name: str = None
    username: str = None
    phone: str = None
    email: str = None
    password: str = None
    photo: str = None


class UserResponseSchema(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    username: str
    phone: str
    email: str
    photo: str
    establishment: establishmentResponseSchema

    class Config:
        from_attributes = True
