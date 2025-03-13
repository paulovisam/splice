from splice.infra.repositories.order_repository import OrderRepository


class DeleteOrder:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def execute(self, order_id: int) -> None:
        await self.order_repo.delete(order_id)
