from splice.infra.repositories.order_repository import OrderRepository


class GetOrder:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def get_by_id(self, order_id: int):
        return await self.order_repo.get_by_id(order_id)
