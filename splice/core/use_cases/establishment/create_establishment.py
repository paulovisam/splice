from splice.core.models.establishment import Establishment
from splice.infra.repositories.establishment_repository import (
    EstablishmentRepository,
)


class CreateEstablishment:
    def __init__(self, establishment_repo: EstablishmentRepository):
        self.repo = establishment_repo

    async def execute(self, name: str, description: str, photo: str, user_id: str):
        new_establishment = Establishment(
            name=name, description=description, photo=photo, user_id=user_id
        )
        return await self.repo.save(new_establishment)
