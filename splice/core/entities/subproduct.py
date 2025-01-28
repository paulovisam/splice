import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from splice.infra.database.base import table_registry

@table_registry.mapped_as_dataclass
class Subproduct():
    __tablename__ = 'subproducts'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    id_product: Mapped[str]
    name: Mapped[str]
    value: Mapped[float]
    amount: Mapped[int]
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, nullable=True, onupdate=func.now()
    )



    def dict(self):
        return {
            'id': self.id,
            'id_product': self.id_product,
            'name': self.name,
            'value': self.value,
            'amount': self.amount,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
