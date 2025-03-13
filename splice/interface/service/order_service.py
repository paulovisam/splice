# app/api/services/order_service.py
from splice.core.use_cases.order import (
    CreateOrder,
    DeleteOrder,
    GetOrder,
    UpdateOrder,
)
from splice.infra.repositories.order_repository import OrderRepository, Order


class OrderService:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    async def create(self, **kwargs) -> Order:
        use_case = CreateOrder(self.repo)
        return await use_case.execute(**kwargs)

    async def get_by_id(self, order_id: int) -> Order | None:
        use_case = GetOrder(self.repo)
        return await use_case.get_by_id(order_id)

    async def get_by_user_id(self, user_id: int) -> Order | None:
        use_case = GetOrder(self.repo)
        return await use_case.get_by_user_id(user_id)

    async def get_by_establishment_id(
        self, establishment_id: int
    ) -> Order | None:
        use_case = GetOrder(self.repo)
        return await use_case.get_by_establishment_id(establishment_id)

    async def update(self, order_id: int, **kwargs) -> Order:
        use_case = UpdateOrder(self.repo)
        return await use_case.execute(order_id=order_id, **kwargs)

    async def delete(self, order_id: int) -> None:
        use_case = DeleteOrder(self.repo)
        return await use_case.execute(order_id)
