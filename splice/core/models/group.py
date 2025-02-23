import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from splice.infra.database.base import BaseTable, Field
from sqlmodel import Relationship
from splice.utils.generate_schemas import generate_schema as _generate_schema
from .linkusergroup import linkUserGroup


class Group(BaseTable, table=True):
    __tablename__ = "groups"
    name: str
    photo: str
    users: list["User"] = Relationship(
        back_populates="groups",
        link_model=linkUserGroup,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


GroupCreateSchema = _generate_schema(Group)
GroupUpdateSchema = _generate_schema(Group, optional=True)
