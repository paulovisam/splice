from splice.infra.repositories.product_repository import ProductRepository


class DeleteProduct:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def execute(self, product_id: int):
        await self.product_repo.delete(product_id)
