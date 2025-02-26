from sqlmodel import Relationship

from splice.infra.database.base import BaseTable
from splice.utils.generate_schemas import generate_schema as _generate_schema

from .linkusergroup import linkUserGroup


class Group(BaseTable, table=True):
    __tablename__ = 'groups'
    name: str
    photo: str
    users: list['User'] = Relationship(  # type: ignore #noqa: F821
        back_populates='groups',
        link_model=linkUserGroup,
        sa_relationship_kwargs={'lazy': 'selectin'},
    )


GroupCreateSchema = _generate_schema(Group)
GroupUpdateSchema = _generate_schema(Group, optional=True)
