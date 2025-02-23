from splice.core.models.establishment import establishment
from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)


class Createestablishment:
    def __init__(self, establishment_repo: establishmentRepository):
        self.repo = establishment_repo

    async def execute(self, name: str, description: str, photo: str, user_id: str):
        new_establishment = establishment(
            name=name, description=description, photo=photo, user_id=user_id
        )
        return await self.repo.save(new_establishment)
