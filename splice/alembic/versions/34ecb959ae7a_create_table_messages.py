"""create_table_messages

Revision ID: 34ecb959ae7a
Revises: c0491bbde3cb
Create Date: 2024-11-14 00:04:56.275542

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID

# revision identifiers, used by Alembic.
revision: str = '34ecb959ae7a'
down_revision: Union[str, None] = 'c0491bbde3cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'messages',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('sender_id', sa.String(), sa.ForeignKey('users.username')),
        sa.Column('receiver_id', sa.String(), sa.ForeignKey('users.username')),
        sa.Column('created_at', TIMESTAMP),
        sa.Column('updated_at', TIMESTAMP, nullable=True),
        # Chaves estrangeiras
        sa.ForeignKeyConstraint(
            ['sender_id'],
            ['users.username'],
            name='fk_messages_sender',
            ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['receiver_id'],
            ['users.username'],
            name='fk_messages_receiver',
            ondelete='CASCADE',
        ),
    )


def downgrade() -> None:
    op.drop_table('messages')
