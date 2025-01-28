from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MessageCreateSchema(BaseModel):
    content: str
    sender: str
    receiver: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None


class MessageUpdateSchema(BaseModel):
    content: str = None
    sender: str = None
    receiver: str = None
    updated_at: datetime = datetime.now()


class MessageResponseSchema(MessageUpdateSchema):
    id: str
    content: Optional[str] = None
    sender: Optional[str] = None
    receiver: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
