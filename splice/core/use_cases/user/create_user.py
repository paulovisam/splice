from splice.core.models.user import User
from splice.infra.repositories.user_repository import UserRepository
from splice.interface.service.auth_service import AuthService


class CreateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def execute(self, **kwargs):
        auth_service = AuthService()
        new_user = User(**kwargs)
        new_user.password = auth_service.get_password_hash(new_user.password)
        return await self.user_repo.save(new_user)
