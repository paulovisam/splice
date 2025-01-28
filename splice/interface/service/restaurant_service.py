from splice.infra.repositories.restaurant_repository import RestaurantRepository
from splice.core.use_cases.restaurant import DeleteRestaurant, CreateRestaurant, GetRestaurant, UpdateRestaurant

class RestaurantService:
    def __init__(self, repo: RestaurantRepository):
        self.repo = repo
    
    async def create_restaurant(
        self,
        name: str,
        description: str,
        photo: str,
        user_id: str
    ):
        use_case = CreateRestaurant(self.repo)
        return await use_case.execute(
            name=name,
            description=description,
            photo=photo,
            user_id=user_id
        )
    
    async def get_restaurant_by_id(
        self,
        restaurant_id: str,
    ):
        use_case = GetRestaurant(restaurant_repo=self.repo)
        return await use_case.execute(restaurant_id=restaurant_id)

    async def get_restaurant_by_user_id(
        self,
        user_id: str,
    ):
        use_case = GetRestaurant(restaurant_repo=self.repo)
        return await use_case.execute(user_id=user_id)


    async def update_restaurant(
        self,
        id: str,
        user_id: str,
        name: str,
        description: str,
        photo: str
    ):
        use_case = UpdateRestaurant(self.repo)
        return await use_case.execute(
            restaurant_id=id,
            user_id=user_id,
            name=name,
            description=description,
            photo=photo
        )
        
    async def delete_restaurant(self, restaurant_id: str):
        use_case = DeleteRestaurant(self.repo)

        return await use_case.execute(restaurant_id)