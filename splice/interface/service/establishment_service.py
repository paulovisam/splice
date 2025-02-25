from splice.core.use_cases.establishment import (
    CreateEstablishment,
    DeleteEstablishment,
    GetEstablishment,
    UpdateEstablishment,
)
from splice.infra.repositories.establishment_repository import (
    EstablishmentRepository,
)


class EstablishmentService:
    def __init__(self, repo: EstablishmentRepository):
        self.repo = repo

    async def create_establishment(
        self, name: str, description: str, photo: str, user_id: str
    ):
        use_case = CreateEstablishment(self.repo)
        return await use_case.execute(
            name=name, description=description, photo=photo, user_id=user_id
        )

    async def get_establishment_by_id(
        self,
        establishment_id: str,
    ):
        use_case = GetEstablishment(establishment_repo=self.repo)
        return await use_case.execute(establishment_id=establishment_id)

    async def get_establishment_by_user_id(
        self,
        user_id: str,
    ):
        use_case = GetEstablishment(establishment_repo=self.repo)
        return await use_case.execute(user_id=user_id)

    async def update_establishment(
        self, id: str, user_id: str, name: str, description: str, photo: str
    ):
        use_case = UpdateEstablishment(self.repo)
        return await use_case.execute(
            establishment_id=id,
            user_id=user_id,
            name=name,
            description=description,
            photo=photo,
        )

    async def delete_establishment(self, establishment_id: str):
        use_case = DeleteEstablishment(self.repo)

        return await use_case.execute(establishment_id)
