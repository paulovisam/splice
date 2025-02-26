from splice.infra.repositories.order_repository import OrderRepository


class GetOrder:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def get_by_id(self, order_id: int):
        return await self.order_repo.get_by_id(order_id)

    async def get_by_user_id(self, user_id: int):
        return await self.order_repo.get_by_user_id(user_id)

    async def get_by_establishment_id(self, establishment_id: int):
        return await self.order_repo.get_by_establishment_id(establishment_id)
