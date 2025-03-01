from splice.infra.repositories.subproduct_repository import (
    SubproductRepository,
)


class DeleteSubproduct:
    def __init__(self, subproduct_repo: SubproductRepository):
        self.subproduct_repo = subproduct_repo

    async def execute(self, subproduct_id: int):
        await self.subproduct_repo.delete(subproduct_id)
