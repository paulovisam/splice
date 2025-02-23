from splice.utils.generate_schemas import generate_schema
from splice.infra.database.base import BaseTable, Field

class Event(BaseTable, table=True):
    __tablename__ = 'events'
    id_establishment: str = Field(nullable=False)
    type_establishment: str
    title: str = Field(nullable=False)
    photo: str
    description: str
    link: str
    type_event: str
    entry_hour: str = Field(nullable=False)
    ending_time: str

EventCreateSchema = generate_schema(Event)
EventUpdateSchema = generate_schema(Event, optional=True)