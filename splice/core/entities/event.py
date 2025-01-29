import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from splice.infra.database.base import table_registry


@table_registry.mapped_as_dataclass
class Event():
    __tablename__ = 'events'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    id_establishment: Mapped[str]
    type_establishment: Mapped[str]
    title: Mapped[str]
    photo: Mapped[str]
    description: Mapped[str]
    link: Mapped[str]
    type_event: Mapped[str]
    entry_hour: Mapped[str]
    ending_time: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, nullable=True, onupdate=func.now()
    )



    def dict(self):
        return {
            'id': self.id,
            'id_establishment':self.id_establishment,
            'type_establishment':self.type_establishment,
            'title':self.title,
            'photo':self.photo,
            'description':self.description,
            'link':self.link,
            'type_event':self.type_event,
            'entry_hour':self.entry_hour,
            'ending_time':self.ending_time,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
