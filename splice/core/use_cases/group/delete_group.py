from splice.infra.repositories.group_repository import GroupRepository


class DeleteGroup:
    def __init__(self, group_repo: GroupRepository):
        self.group_repo = group_repo

    async def execute(self, group_id: int):
        await self.group_repo.delete(group_id)
