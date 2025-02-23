from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)


class Deleteestablishment:
    def __init__(self, repo: establishmentRepository):
        self.repo = repo

    async def execute(self, establishment_id: int):
        await self.repo.delete(establishment_id)
