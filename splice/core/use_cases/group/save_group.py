from splice.core.models.group import Group
from splice.infra.repositories.group_repository import GroupRepository


class SaveGroup:
    def __init__(self, group_repo: GroupRepository):
        self.group_repo = group_repo

    async def execute(self, name: str, photo: str):
        new_group = Group(name=name, photo=photo)
        return await self.group_repo.save(new_group)
