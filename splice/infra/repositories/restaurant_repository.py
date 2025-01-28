from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.entities.restaurant import Restaurant


class RestaurantRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, restaurant: Restaurant) -> Restaurant:
        async with self.db_session() as session:
            if restaurant.id is None:
                session.add(restaurant)
            else:
                await session.merge(restaurant)
            await session.commit()
            return restaurant

    async def get_by_id(self, restaurant_id: int) -> Restaurant | None:
        async with self.db_session() as session:
            statement = select(Restaurant).filter_by(id=restaurant_id)
            return (await session.execute(statement)).scalar_one_or_none()

    async def get_by_user_id(self, user_id: int) -> Restaurant | None:
        async with self.db_session() as session:
            statement = select(Restaurant).filter_by(user_id=user_id)
            return (await session.execute(statement)).scalar_one_or_none()

    async def delete(self, restaurant_id: int) -> None:
        async with self.db_session() as session:
            statement = select(Restaurant).filter_by(id=restaurant_id)
            restaurant = (await session.execute(statement)).scalar_one_or_none()
        if restaurant:
            await session.delete(restaurant)
            await session.commit()
