from splice.core.models.establishment import Establishment
from splice.infra.repositories.establishment_repository import (
    EstablishmentRepository,
)


class GetEstablishment:
    def __init__(self, establishment_repo: EstablishmentRepository):
        self.repo = establishment_repo

    async def execute(
        self,
        establishment_id: str = None,
        user_id: str = None,
    ) -> Establishment | None:
        if establishment_id:
            return await self.repo.get_by_id(establishment_id=establishment_id)
        if user_id:
            return await self.repo.get_by_user_id(user_id=user_id)
