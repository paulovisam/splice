import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from splice.infra.database.base import table_registry


@table_registry.mapped_as_dataclass
class Message:
    __tablename__ = 'messages'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), init=False, primary_key=True, default=uuid.uuid4
    )
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, nullable=True, onupdate=func.now()
    )

    sender_id: Mapped[str] = mapped_column(ForeignKey('users.username'))
    receiver_id: Mapped[str] = mapped_column(ForeignKey('users.username'))

    # Relationships
    sender: Mapped['User'] = relationship(
        'User', foreign_keys=[sender_id], back_populates='sent_messages'
    )
    receiver: Mapped['User'] = relationship(
        'User', foreign_keys=[receiver_id], back_populates='received_messages'
    )

    # sender: Mapped["User"] = relationship(
    #     "User", back_populates="sent_messages", foreign_keys=[sender_id]
    # )
    # receiver: Mapped["User"] = relationship(
    #     "User", back_populates="received_messages", foreign_keys=[receiver_id]
    # )

    def dict(self):
        return {
            'id': self.id,
            'sender': self.sender.username if self.sender else None,
            'receiver': self.receiver.username if self.receiver else None,
            'receiver': self.receiver,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
