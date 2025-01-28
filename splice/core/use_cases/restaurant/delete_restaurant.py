from splice.infra.repositories.restaurant_repository import RestaurantRepository


class DeleteRestaurant:
    def __init__(self, repo: RestaurantRepository):
        self.repo = repo

    async def execute(self, restaurant_id: int):
        await self.repo.delete(restaurant_id)
