from splice.infra.repositories.group_repository import GroupRepository


class GetGroup:
    def __init__(self, group_repo: GroupRepository):
        self.group_repo = group_repo

    async def get_by_id(self, user_id: int):
        return await self.group_repo.get_by_id(user_id)
