from uuid import UUID

from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, Any


class MessageCreateSchema(BaseModel):
    content: str
    sender: str
    receiver: str


class MessageUpdateSchema(BaseModel):
    content: str = None
    sender: str = None
    receiver: str = None


class MessageResponseSchema(MessageCreateSchema):
    id: str
