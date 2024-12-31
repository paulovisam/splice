# app/api/schemas/user_schema.py
from uuid import UUID

from pydantic import BaseModel


class GroupCreateSchema(BaseModel):
    name: str
    photo: str


class GroupUpdateSchema(BaseModel):
    id: UUID = None
    name: str = None
    photo: str = None


class GroupResponseSchema(GroupUpdateSchema):
    class Config:
        from_attributes = True
