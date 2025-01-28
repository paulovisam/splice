import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from splice.infra.database.base import table_registry

@table_registry.mapped_as_dataclass
class Restaurant():
    __tablename__ = 'restaurants'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    id_user: Mapped[str]
    description: Mapped[str]
    name: Mapped[str]
    category: Mapped[str]
    photo: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, nullable=True, onupdate=func.now()
    )



    def dict(self):
        return {
            'id': self.id,
            'id_user': self.id_user,
            'description': self.description,
            'name': self.name,
            'category': self.category,
            'photo': self.photo,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
