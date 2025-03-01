# app/api/services/subproduct_service.py
from splice.core.use_cases.subproduct import (
    CreateSubproduct,
    DeleteSubproduct,
    GetSubproduct,
    UpdateSubproduct,
)
from splice.infra.repositories.subproduct_repository import (
    SubproductRepository,
)


class SubproductService:
    def __init__(self, repo: SubproductRepository):
        self.repo = repo

    async def create(self, **kwargs):
        use_case = CreateSubproduct(self.repo)
        return await use_case.execute(**kwargs)

    async def get_by_id(self, subproduct_id: int):
        use_case = GetSubproduct(self.repo)
        return await use_case.get_by_id(subproduct_id)

    async def update(self, subproduct_id: int, **kwargs):
        use_case = UpdateSubproduct(self.repo)
        return await use_case.execute(subproduct_id=subproduct_id, **kwargs)

    async def delete(self, subproduct_id: int):
        use_case = DeleteSubproduct(self.repo)
        return await use_case.execute(subproduct_id)
