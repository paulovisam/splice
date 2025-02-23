from splice.core.use_cases.establishment import (
    Createestablishment,
    Deleteestablishment,
    Getestablishment,
    Updateestablishment,
)
from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)


class establishmentService:
    def __init__(self, repo: establishmentRepository):
        self.repo = repo

    async def create_establishment(
        self,
        name: str,
        description: str,
        photo: str,
        user_id: str
    ):
        use_case = Createestablishment(self.repo)
        return await use_case.execute(
            name=name,
            description=description,
            photo=photo,
            user_id=user_id
        )

    async def get_establishment_by_id(
        self,
        establishment_id: str,
    ):
        use_case = Getestablishment(establishment_repo=self.repo)
        return await use_case.execute(establishment_id=establishment_id)

    async def get_establishment_by_user_id(
        self,
        user_id: str,
    ):
        use_case = Getestablishment(establishment_repo=self.repo)
        return await use_case.execute(user_id=user_id)

    async def update_establishment(
        self,
        id: str,
        user_id: str,
        name: str,
        description: str,
        photo: str
    ):
        use_case = Updateestablishment(self.repo)
        return await use_case.execute(
            establishment_id=id,
            user_id=user_id,
            name=name,
            description=description,
            photo=photo
        )

    async def delete_establishment(self, establishment_id: str):
        use_case = Deleteestablishment(self.repo)

        return await use_case.execute(establishment_id)
