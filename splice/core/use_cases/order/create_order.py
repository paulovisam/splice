from splice.core.models.order import Order
from splice.infra.repositories.order_repository import OrderRepository


class CreateOrder:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def execute(
        self,
        # dados do order
    ):
        new_order = Order(
            # dados do order
        )
        return await self.order_repo.save(new_order)
