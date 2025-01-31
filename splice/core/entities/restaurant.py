import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from splice.infra.database.base import table_registry


@table_registry.mapped_as_dataclass
class Restaurant:
    __tablename__ = 'restaurants'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )

    name: Mapped[str]
    description: Mapped[str]
    photo: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, nullable=True, onupdate=func.now()
    )

    # Relação com a tabela 'users'
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )

    # user: Mapped["User"] = relationship("User", backref="restaurants", uselist=False, init=False, lazy='joined')
