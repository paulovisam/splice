from splice.infra.repositories.group_repository import GroupRepository


class UpdateGroup:
    def __init__(self, group_repo: GroupRepository):
        self.group_repo = group_repo

    async def execute(self, group_id: str, **kwargs):
        # Obtém o grupo pelo ID
        group = await self.group_repo.get_by_id(group_id)

        if not group:
            raise ValueError('Grupo não encontrado')

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(group, key):
                setattr(group, key, value)

        return await self.group_repo.save(group)
