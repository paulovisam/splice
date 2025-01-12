"""create_table_groups

Revision ID: 5f4e05f9021f
Revises: c0491bbde3cb
Create Date: 2024-11-14 00:48:42.411076

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '5f4e05f9021f'
down_revision: Union[str, None] = '34ecb959ae7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'groups',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('photo', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('groups')


''
