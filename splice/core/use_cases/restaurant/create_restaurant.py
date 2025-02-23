from splice.core.models.restaurant import Restaurant
from splice.infra.repositories.restaurant_repository import (
    RestaurantRepository,
)


class CreateRestaurant:
    def __init__(self, restaurant_repo: RestaurantRepository):
        self.repo = restaurant_repo

    async def execute(
        self,
        name: str,
        description: str,
        photo: str,
        user_id: str
    ):
        new_restaurant = Restaurant(
            name=name,
            description=description,
            photo=photo,
            user_id=user_id
        )
        return await self.repo.save(new_restaurant)
