from splice.core.models.restaurant import Restaurant
from splice.infra.repositories.restaurant_repository import (
    RestaurantRepository,
)


class GetRestaurant:
    def __init__(self, restaurant_repo: RestaurantRepository):
        self.repo = restaurant_repo

    async def execute(
        self,
        restaurant_id: str = None,
        user_id: str = None,
    ) -> Restaurant | None:
        if restaurant_id:
            return await self.repo.get_by_id(restaurant_id=restaurant_id)
        if user_id:
            return await self.repo.get_by_user_id(user_id=user_id)
