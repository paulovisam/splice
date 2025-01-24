"""create_table_notification

Revision ID: 18e467d842dc
Revises: 5f4e05f9021f
Create Date: 2024-12-30 21:56:24.180912

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '18e467d842dc'
down_revision: Union[str, None] = '5f4e05f9021f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'notification',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('message_id', sa.String(), sa.ForeignKey('users.username')),
        sa.Column('user_id', sa.String(), sa.ForeignKey('users.username')),
        sa.Column('is_read', sa.Boolean()),
    )


def downgrade() -> None:
    pass
