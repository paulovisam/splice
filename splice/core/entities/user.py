import uuid
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from splice.infra.database.base import table_registry


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    photo: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, nullable=True, onupdate=func.now()
    )

    restaurant: Mapped['Restaurant'] = relationship(
        "Restaurant", backref="user", cascade="all, delete-orphan", lazy='joined', init=False
    )

    groups: Mapped[list["Group"]] = relationship(
        'Group',
        secondary='user_groups',
        back_populates='users',
        default_factory=list,
        lazy='joined'
    )

    def dict(self, include_groups=True):
        user_dict = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'username': self.username,
            'photo': self.photo,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        if include_groups:
            user_dict['groups'] = [group.dict(include_users=False) for group in self.groups]
        return user_dict
