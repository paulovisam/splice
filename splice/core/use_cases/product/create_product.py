from splice.core.models.product import Product
from splice.infra.repositories.product_repository import ProductRepository


class CreateProduct:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def execute(self, **kwargs):
        new_product = Product(**kwargs)
        return await self.product_repo.save(new_product)
