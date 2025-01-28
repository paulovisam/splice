"""create_table_restaurant

Revision ID: 461c087a6642
Revises: c0491bbde3cb
Create Date: 2025-01-05 15:56:57.160801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID


# revision identifiers, used by Alembic.
revision: str = '461c087a6642'
down_revision: Union[str, None] = 'c0491bbde3cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'restaurants',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id')),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.Column('photo', sa.String()),
        sa.Column('created_at', TIMESTAMP),
        sa.Column('updated_at', TIMESTAMP, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('restaurant')
