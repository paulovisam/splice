from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.entities.restaurant import Restaurant


class RestaurantRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, restaurant: Restaurant) -> Restaurant:
        print("save restaurant ",restaurant.dict());
        from uuid import uuid4
        restaurant.id = str(uuid4())
        return restaurant
        # async with self.db_session() as session:
        #     if restaurant.id is None:
        #         # Inserir novo
        #         session.add(restaurant)
        #     else:
        #         # Atualizar existente
        #         await session.merge(restaurant)
        #     await session.commit()
        #     return restaurant

    async def get_by_id(self, restaurant_id: int) -> Restaurant | None:
        print("get restaurant "+restaurant_id);
        restaurant = Restaurant("user","description","resturante do ze","NONE","")
        return restaurant
        # async with self.db_session() as session:
        #     statement = select(Restaurant).filter_by(id=restaurant_id)
        #     return (await session.execute(statement)).scalar_one_or_none()

    async def delete(self, restaurant_id: int) -> None:
        print("delete restaurant "+restaurant_id);
        # async with self.db_session() as session:
        #     statement = select(Restaurant).filter_by(id=restaurant_id)
        #     restaurant = (await session.execute(statement)).scalar_one_or_none()
        # if restaurant:
        #     await session.delete(restaurant)
        #     await session.commit()
