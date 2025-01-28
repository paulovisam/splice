# app/api/services/subproduct_service.py
from splice.core.use_cases.subproduct.create_subproduct import CreateSubproduct
from splice.core.use_cases.subproduct.delete_subproduct import DeleteSubproduct
from splice.core.use_cases.subproduct.get_subproduct import GetSubproduct
from splice.core.use_cases.subproduct.update_subproduct import UpdateSubproduct
from splice.infra.repositories.subproduct_repository import SubproductRepository


class SubproductService:
    def __init__(self, repo: SubproductRepository):
        self.repo = repo

    async def create(
        self,
        id_product: str,
        name: str,
        value: float,
        amount: int,
        description: str

    ):
        use_case = CreateSubproduct(self.repo)
        return await use_case.execute(
            id_product=id_product,
            name=name,
            value=value,
            amount=amount,
            description=description,
        )
    async def get_by_id(self, subproduct_id: int):
        use_case = GetSubproduct(self.repo)
        return await use_case.get_by_id(subproduct_id)

    async def update(self, subproduct_id: int, **kwargs):
        use_case = UpdateSubproduct(self.repo)
        return await use_case.execute(subproduct_id=subproduct_id, **kwargs)

    async def delete(self, subproduct_id: int):
        use_case = DeleteSubproduct(self.repo)
        return await use_case.execute(subproduct_id)
