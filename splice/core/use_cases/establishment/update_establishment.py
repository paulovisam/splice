from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)


class Updateestablishment:
    def __init__(self, establishment_repo: establishmentRepository):
        self.repo = establishment_repo

    async def execute(self, establishment_id: str, **kwargs):
        # Obtém o usuário pelo ID
        establishment = await self.repo.get_by_id(establishment_id)

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(establishment, key):
                setattr(establishment, key, value)

        return await self.repo.save(establishment)
