from splice.core.models.user import User
from splice.infra.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def execute(self, **kwargs):
        new_user = User(**kwargs)
        return await self.user_repo.save(new_user)
