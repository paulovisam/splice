from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.models.establishment import Establishment


class EstablishmentRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, establishment: Establishment) -> Establishment:
        await self.db_session.merge(establishment)
        await self.db_session.commit()
        return establishment

    # TODO = corrigir type para uuid
    async def get_by_id(self, establishment_id: int) -> Establishment | None:
        statement = select(Establishment).filter_by(id=establishment_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def get_by_user_id(self, user_id: int) -> Establishment | None:
        statement = select(Establishment).filter_by(user_id=user_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def delete(self, establishment_id: int) -> None:
        statement = select(Establishment).filter_by(id=establishment_id)
        establishment = (
            await self.db_session.execute(statement)
        ).scalar_one_or_none()
        if establishment:
            await self.db_session.delete(establishment)
            await self.db_session.commit()
