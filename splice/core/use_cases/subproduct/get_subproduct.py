from splice.infra.repositories.subproduct_repository import SubproductRepository


class GetSubproduct:
    def __init__(self, subproduct_repo: SubproductRepository):
        self.subproduct_repo = subproduct_repo

    async def get_by_id(self, subproduct_id: int):
        return await self.subproduct_repo.get_by_id(subproduct_id)
