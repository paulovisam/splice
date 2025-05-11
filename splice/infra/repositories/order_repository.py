from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from splice.core.models.order import Order


class OrderRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, order: Order) -> Order:
        await self.db_session.merge(order)
        await self.db_session.commit()
        return order

    async def get_by_id(self, order_id: UUID) -> Order | None:
        statement = select(Order).filter_by(id=order_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def get_by_user_id(
        self, user_id: UUID, offset: int, limit: int
    ) -> Order | None:
        statement = (
            select(Order)
            .filter_by(user_id=user_id)
            .offset(offset)
            .limit(limit)
        )
        return (await self.db_session.execute(statement)).scalars().all()

    async def get_by_establishment_id(
        self, establishment_id: UUID, offset: int, limit: int
    ) -> Order | None:
        statement = (
            select(Order)
            .filter_by(establishment_id=establishment_id)
            .offset(offset)
            .limit(limit)
        )
        return (await self.db_session.execute(statement)).scalars().all()

    async def delete(self, order_id: UUID) -> None:
        statement = select(Order).filter_by(id=order_id)
        order = (await self.db_session.execute(statement)).scalar_one_or_none()
        if order:
            await self.db_session.delete(order)
            await self.db_session.commit()

    async def count_by_user_id(self, user_id: str) -> int:
        statement = select(func.count()).filter(Order.user_id == user_id)
        result = await self.db_session.execute(statement)
        return result.scalar()

    async def count_by_establishment_id(self, establishment_id: str) -> int:
        statement = select(func.count()).filter(
            Order.establishment_id == establishment_id
        )
        result = await self.db_session.execute(statement)
        return result.scalar()
