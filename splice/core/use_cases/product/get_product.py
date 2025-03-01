from splice.infra.repositories.product_repository import ProductRepository


class GetProduct:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def get_by_id(self, product_id: int):
        return await self.product_repo.get_by_id(product_id)
