from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.entities.group import Group


class GroupRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, group: Group) -> Group:
        async with self.db_session() as session:
            if group.id is None:
                # Inserir novo group
                session.add(group)
            else:
                # Atualizar group existente
                await session.merge(group)
            await session.commit()
            return group

    async def get_by_id(self, group_id: int) -> Group | None:
        async with self.db_session() as session:
            statement = select(Group).filter_by(id=group_id)
            return (await session.execute(statement)).scalar_one_or_none()

    async def delete(self, group_id: int) -> None:
        async with self.db_session() as session:
            statement = select(Group).filter_by(id=group_id)
            group = (await session.execute(statement)).scalar_one_or_none()
        if group:
            await session.delete(group)
            await session.commit()
