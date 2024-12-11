from pydantic import BaseModel


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
