from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID

from splice.infra.database.base import table_registry

# 📌 Definindo a tabela associativa corretamente
user_groups = Table(
    'user_groups',  # Nome da tabela
    table_registry.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('group_id', UUID(as_uuid=True), ForeignKey('groups.id'), primary_key=True)
)
