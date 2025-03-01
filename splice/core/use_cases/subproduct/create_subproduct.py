from splice.core.models.subproduct import Subproduct
from splice.infra.repositories.subproduct_repository import (
    SubproductRepository,
)


class CreateSubproduct:
    def __init__(self, subproduct_repo: SubproductRepository):
        self.subproduct_repo = subproduct_repo

    async def execute(self, **kwargs):
        new_subproduct = Subproduct(**kwargs)
        return await self.subproduct_repo.save(new_subproduct)
