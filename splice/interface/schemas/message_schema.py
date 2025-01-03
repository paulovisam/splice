from pydantic import BaseModel
from typing import Optional


class MessageCreateSchema(BaseModel):
    content: str
    sender: str
    receiver: str


class MessageUpdateSchema(BaseModel):
    content: str = None
    sender: str = None
    receiver: str = None


class MessageResponseSchema(BaseModel):
    id: str
    content: Optional[str] = None
    sender: Optional[str] = None
    receiver: Optional[str] = None
