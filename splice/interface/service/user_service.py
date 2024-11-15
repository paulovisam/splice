# app/api/services/user_service.py
from splice.core.use_cases.user.create_user import CreateUser
from splice.core.use_cases.user.delete_user import DeleteUser
from splice.core.use_cases.user.get_user import GetUser
from splice.core.use_cases.user.update_user import UpdateUser
from splice.infra.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        username: str,
        password: str,
        photo: str,
    ):
        use_case = CreateUser(self.repo)
        return await use_case.execute(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            username=username,
            password=password,
            photo=photo,
        )

    async def get_user_by_id(self, user_id: int):
        use_case = GetUser(self.repo)
        return await use_case.get_by_id(user_id)

    async def get_user_by_username(self, username: str):
        use_case = GetUser(self.repo)
        return await use_case.get_by_username(username=username)

    async def get_user_by_email(self, email: str):
        use_case = GetUser(self.repo)
        return await use_case.get_by_email(email=email)

    async def get_user_by_phone(self, phone: str):
        use_case = GetUser(self.repo)
        return await use_case.get_by_phone(phone=phone)

    async def update_user(self, user_id: int, **kwargs):
        use_case = UpdateUser(self.repo)
        return await use_case.execute(user_id=user_id, **kwargs)

    async def delete_user(self, user_id: int):
        use_case = DeleteUser(self.repo)
        return await use_case.execute(user_id)
