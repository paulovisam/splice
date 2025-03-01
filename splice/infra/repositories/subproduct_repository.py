from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.models.subproduct import Subproduct


class SubproductRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, subproduct: Subproduct) -> Subproduct:
        await self.db_session.merge(subproduct)
        await self.db_session.commit()
        return subproduct

    async def get_by_id(self, subproduct_id: int) -> Subproduct | None:
        statement = select(Subproduct).filter_by(id=subproduct_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def delete(self, subproduct_id: int) -> None:
        statement = select(Subproduct).filter_by(id=subproduct_id)
        subproduct = (
            await self.db_session.execute(statement)
        ).scalar_one_or_none()
        if subproduct:
            await self.db_session.delete(subproduct)
            await self.db_session.commit()
