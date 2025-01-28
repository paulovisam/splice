from splice.infra.repositories.subproduct_repository import SubproductRepository


class UpdateSubproduct:
    def __init__(self, subproduct_repo: SubproductRepository):
        self.subproduct_repo = subproduct_repo

    async def execute(self, subproduct_id: str, **kwargs):
        # Obtém  pelo ID
        subproduct = await self.subproduct_repo.get_by_id(subproduct_id)

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(subproduct, key):
                setattr(subproduct, key, value)

        return await self.subproduct_repo.save(subproduct)
