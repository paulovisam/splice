from splice.core.entities.user import User
from splice.infra.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def execute(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        username: str,
        password: str,
        photo: str,
    ):
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            username=username,
            password=password,
            photo=photo,
        )
        return await self.user_repo.save(new_user)
