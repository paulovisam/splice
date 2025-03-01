from splice.infra.repositories.product_repository import ProductRepository


class UpdateProduct:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def execute(self, product_id: str, **kwargs):
        # Obtém  pelo ID
        product = await self.product_repo.get_by_id(product_id)

        if not product:
            raise ValueError('Produto não encontrado')

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(product, key):
                setattr(product, key, value)

        return await self.product_repo.save(product)
