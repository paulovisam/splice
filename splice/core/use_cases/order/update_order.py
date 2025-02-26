from splice.infra.repositories.order_repository import OrderRepository


class UpdateOrder:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def execute(self, order_id: str, **kwargs):
        # Obtém  pelo ID
        order = await self.order_repo.get_by_id(order_id)

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(order, key):
                setattr(order, key, value)

        return await self.order_repo.save(order)
