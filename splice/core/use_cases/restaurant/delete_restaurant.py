from splice.infra.repositories.restaurant_repository import RestaurantRepository


class DeleteRestaurant:
    def __init__(self, restaurant_repo: RestaurantRepository):
        self.restaurant_repo = restaurant_repo

    async def execute(self, restaurant_id: int):
        await self.restaurant_repo.delete(restaurant_id)
