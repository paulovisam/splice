import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from splice.infra.database.base import table_registry


@table_registry.mapped_as_dataclass
class Group:
    __tablename__ = 'groups'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str]
    photo: Mapped[str]

    users: Mapped[list["User"]] = relationship(
        'User',
        secondary='user_groups',
        back_populates='groups',
        default_factory=list,
        lazy='joined'
    )

    def dict(self, include_users=True):
        group_dict = {
            'id': self.id,
            'name': self.name,
            'photo': self.photo,
        }
        if include_users:
            group_dict["users"] = [user.dict(include_groups=False) for user in self.users]
        return group_dict
