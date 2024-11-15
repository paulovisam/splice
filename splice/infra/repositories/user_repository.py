from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.entities.user import User


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, user: User) -> User:
        async with self.db_session() as session:
            if user.id is None:
                # Inserir novo usuário
                session.add(user)
            else:
                # Atualizar usuário existente
                await session.merge(user)
            await session.commit()
            return user

    async def get_by_id(self, user_id: int) -> User | None:
        async with self.db_session() as session:
            statement = select(User).filter_by(id=user_id)
            return (await session.execute(statement)).scalar_one_or_none()

    async def get_by_username(self, username: str) -> User | None:
        async with self.db_session() as session:
            statement = select(User).filter_by(username=username)
            return (await session.execute(statement)).scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        async with self.db_session() as session:
            statement = select(User).filter_by(email=email)
            return (await session.execute(statement)).scalar_one_or_none()

    async def get_by_phone(self, phone: str) -> User | None:
        async with self.db_session() as session:
            statement = select(User).filter_by(phone=phone)
            return (await session.execute(statement)).scalar_one_or_none()

    async def delete(self, user_id: int) -> None:
        async with self.db_session() as session:
            statement = select(User).filter_by(id=user_id)
            user = (await session.execute(statement)).scalar_one_or_none()
        if user:
            await session.delete(user)
            await session.commit()
