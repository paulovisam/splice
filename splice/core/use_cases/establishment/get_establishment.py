from splice.core.models.establishment import establishment
from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)


class Getestablishment:
    def __init__(self, establishment_repo: establishmentRepository):
        self.repo = establishment_repo

    async def execute(
        self,
        establishment_id: str = None,
        user_id: str = None,
    ) -> establishment | None:
        if establishment_id:
            return await self.repo.get_by_id(establishment_id=establishment_id)
        if user_id:
            return await self.repo.get_by_user_id(user_id=user_id)
