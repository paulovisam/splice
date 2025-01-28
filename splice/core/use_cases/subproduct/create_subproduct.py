from splice.core.entities.subproduct import Subproduct
from splice.infra.repositories.subproduct_repository import SubproductRepository


class CreateSubproduct:
    def __init__(self, subproduct_repo: SubproductRepository):
        self.subproduct_repo = subproduct_repo

    async def execute(
        self,
        id_product: str,
        name: str,
        value: float,
        amount: int,
        description: str
    ):
        new_subproduct = Subproduct(
            id_product=id_product,
            name=name,
            value=value,
            amount=amount,
            description=description,
        )
        return await self.subproduct_repo.save(new_subproduct)
