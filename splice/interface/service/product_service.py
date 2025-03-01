# app/api/services/product_service.py
from splice.core.use_cases.product import (
    CreateProduct,
    DeleteProduct,
    GetProduct,
    UpdateProduct,
)
from splice.infra.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    async def create(self, **kwargs):
        use_case = CreateProduct(self.repo)
        return await use_case.execute(**kwargs)

    async def get_by_id(self, product_id: int):
        use_case = GetProduct(self.repo)
        return await use_case.get_by_id(product_id)

    async def update(self, product_id: int, **kwargs):
        use_case = UpdateProduct(self.repo)
        return await use_case.execute(product_id=product_id, **kwargs)

    async def delete(self, product_id: int):
        use_case = DeleteProduct(self.repo)
        return await use_case.execute(product_id)
