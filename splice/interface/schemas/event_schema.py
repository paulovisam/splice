# app/api/schemas/event_schema.py
from pydantic import BaseModel
from uuid import UUID

class EventCreateSchema(BaseModel):
    id_establishment: str
    type_establishment: str
    title: str
    photo: str
    description: str
    link: str
    type_event: str
    entry_hour: str
    ending_time: str

class EventUpdateSchema(BaseModel):
    id: str
    id_establishment: str = None
    type_establishment: str = None
    title: str = None
    photo: str = None
    description: str = None
    link: str = None
    type_event: str = None
    entry_hour: str = None
    ending_time: str = None

class EventResponseSchema(EventCreateSchema):
    id: UUID

    class Config:
        from_attributes = True
