from splice.core.use_cases.group.delete_group import DeleteGroup
from splice.core.use_cases.group.get_group import GetGroup
from splice.core.use_cases.group.save_group import SaveGroup
from splice.core.use_cases.group.update_group import UpdateGroup
from splice.infra.repositories.group_repository import GroupRepository


class GroupService:
    def __init__(self, repo: GroupRepository):
        self.repo = repo

    async def save_group(
        self,
        name: str,
        photo: str,
    ):
        use_case = SaveGroup(self.repo)
        return await use_case.execute(
            name=name,
            photo=photo,
        )

    async def get_by_id(self, group_id: int):
        use_case = GetGroup(self.repo)
        return await use_case.get_by_id(group_id)

    async def update_group(self, group_id: int, **kwargs):
        use_case = UpdateGroup(self.repo)
        return await use_case.execute(group_id=group_id, **kwargs)

    async def delete_group(self, group_id: int):
        use_case = DeleteGroup(self.repo)
        return await use_case.execute(group_id)
