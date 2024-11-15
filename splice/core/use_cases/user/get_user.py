from splice.infra.repositories.user_repository import UserRepository


class GetUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_by_id(self, user_id: int):
        return await self.user_repo.get_by_id(user_id)

    async def get_by_username(self, username: str):
        return await self.user_repo.get_by_username(username)

    async def get_by_email(self, email: str):
        return await self.user_repo.get_by_email(email)

    async def get_by_phone(self, phone: str):
        return await self.user_repo.get_by_phone(phone)
