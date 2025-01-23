
from pydantic import BaseModel


class NotificationCreateSchema(BaseModel):
    message_id: str
    user_id: str
    is_read: bool


class NotificationUpdateSchema(BaseModel):
    message_id: str = None
    user_id: str = None
    is_read: bool = False


class NotificationResponseSchema(NotificationUpdateSchema):
    id: str = None
