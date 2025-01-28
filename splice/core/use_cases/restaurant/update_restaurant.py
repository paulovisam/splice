from splice.infra.repositories.restaurant_repository import RestaurantRepository


class UpdateRestaurant:
    def __init__(self, restaurant_repo: RestaurantRepository):
        self.restaurant_repo = restaurant_repo

    async def execute(self, restaurant_id: str, **kwargs):
        # Obtém  pelo ID
        restaurant = await self.restaurant_repo.get_by_id(restaurant_id)

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(restaurant, key):
                setattr(restaurant, key, value)

        return await self.restaurant_repo.save(restaurant)
