from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.models.restaurant import Restaurant


class RestaurantRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, restaurant: Restaurant) -> Restaurant:
        if restaurant.id is None:
            self.db_session.add(restaurant)
        else:
            await self.db_session.merge(restaurant)
        await self.db_session.commit()
        return restaurant

    async def get_by_id(self, restaurant_id: int) -> Restaurant | None:
        statement = select(Restaurant).filter_by(id=restaurant_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def get_by_user_id(self, user_id: int) -> Restaurant | None:
        statement = select(Restaurant).filter_by(user_id=user_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def delete(self, restaurant_id: int) -> None:
        statement = select(Restaurant).filter_by(id=restaurant_id)
        restaurant = (await self.db_session.execute(statement)).scalar_one_or_none()
        if restaurant:
            await self.db_session.delete(restaurant)
            await self.db_session.commit()
