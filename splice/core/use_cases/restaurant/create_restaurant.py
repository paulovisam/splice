from splice.core.entities.restaurant import Restaurant
from splice.infra.repositories.restaurant_repository import RestaurantRepository


class CreateRestaurant:
    def __init__(self, restaurant_repo: RestaurantRepository):
        self.restaurant_repo = restaurant_repo

    async def execute(
        self,
        id_user: str,
        description: str,
        name: str,
        category: str,
        photo: str,
    ):
        new_restaurant = Restaurant(
            id_user=id_user,
            description=description,
            name=name,
            category=category,
            photo=photo,
        )
        return await self.restaurant_repo.save(new_restaurant)
