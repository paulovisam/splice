"""create_table_usergroups

Revision ID: cd5c12d69355
Revises: 5f4e05f9021f
Create Date: 2025-01-30 22:19:33.953987

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = 'cd5c12d69355'
down_revision: Union[str, None] = '5f4e05f9021f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_groups',
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('group_id', UUID(as_uuid=True), sa.ForeignKey('groups.id'), primary_key=True),
    )


def downgrade() -> None:
    op.drop_table('user_groups')
