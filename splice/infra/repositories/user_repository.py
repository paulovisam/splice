# app/infrastructure/repositories/user_repository_impl.py
from sqlalchemy.orm import Session

from splice.core.entities.user import User


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def salvar(self, user: User) -> User:
        if user.id is None:
            # Inserir novo usuário
            self.db_session.add(user)
        else:
            # Atualizar usuário existente
            self.db_session.merge(user)
        await self.db_session.commit()
        return user

    async def get_by_id(self, user_id: int) -> User:
        return self.db_session.query(User).filter_by(id=user_id).first()

    async def deletar(self, user_id: int) -> None:
        user = self.db_session.query(User).filter_by(id=user_id).first()
        if user:
            self.db_session.delete(user)
            await self.db_session.commit()
