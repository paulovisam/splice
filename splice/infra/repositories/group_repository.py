from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.models.group import Group


class GroupRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, group: Group) -> Group:
        await self.db_session.merge(group)
        await self.db_session.commit()
        return group

    async def get_by_id(self, group_id: int) -> Group | None:
        statement = select(Group).filter_by(id=group_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def delete(self, group_id: int) -> None:
        statement = select(Group).filter_by(id=group_id)
        group = (await self.db_session.execute(statement)).scalar_one_or_none()
        if group:
            await self.db_session.delete(group)
            await self.db_session.commit()
