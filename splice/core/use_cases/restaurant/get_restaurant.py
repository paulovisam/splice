from splice.infra.repositories.restaurant_repository import RestaurantRepository


class GetRestaurant:
    def __init__(self, restaurant_repo: RestaurantRepository):
        self.restaurant_repo = restaurant_repo

    async def get_by_id(self, restaurant_id: int):
        return await self.restaurant_repo.get_by_id(restaurant_id)
