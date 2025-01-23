import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from splice.infra.database.base import table_registry


@table_registry.mapped_as_dataclass
class Group:
    __tablename__ = 'groups'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str]
    photo: Mapped[str]

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'photo': self.photo,
        }
