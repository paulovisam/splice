# app/api/services/restaurant_service.py
from splice.core.use_cases.restaurant.create_restaurant import CreateRestaurant
from splice.core.use_cases.restaurant.delete_restaurant import DeleteRestaurant
from splice.core.use_cases.restaurant.get_restaurant import GetRestaurant
from splice.core.use_cases.restaurant.update_restaurant import UpdateRestaurant
from splice.infra.repositories.restaurant_repository import RestaurantRepository


class RestaurantService:
    def __init__(self, repo: RestaurantRepository):
        self.repo = repo

    async def create(
        self,
        id_user: str,
        description: str,
        name: str,
        category: str,
        photo: str,

    ):
        use_case = CreateRestaurant(self.repo)
        return await use_case.execute(
            id_user=id_user,
            description=description,
            name=name,
            category=category,
            photo=photo,
        )
    async def get_by_id(self, restaurant_id: int):
        use_case = GetRestaurant(self.repo)
        return await use_case.get_by_id(restaurant_id)

    async def update(self, restaurant_id: int, **kwargs):
        use_case = UpdateRestaurant(self.repo)
        return await use_case.execute(restaurant_id=restaurant_id, **kwargs)

    async def delete(self, restaurant_id: int):
        use_case = DeleteRestaurant(self.repo)
        return await use_case.execute(restaurant_id)
