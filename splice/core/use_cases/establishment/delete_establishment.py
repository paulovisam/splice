from splice.infra.repositories.establishment_repository import (
    EstablishmentRepository,
)


class DeleteEstablishment:
    def __init__(self, repo: EstablishmentRepository):
        self.repo = repo

    async def execute(self, establishment_id: int):
        await self.repo.delete(establishment_id)
