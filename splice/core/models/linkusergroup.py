import uuid

from splice.infra.database.base import Field, SQLModel


class linkUserGroup(SQLModel, table=True):
    user_id: uuid.UUID = Field(default=None, foreign_key="users.id", primary_key=True)
    group_id: uuid.UUID = Field(default=None, foreign_key="groups.id", primary_key=True)
