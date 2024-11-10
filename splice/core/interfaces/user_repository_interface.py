# app/core/interfaces/user_repository_interface.py
from abc import ABC, abstractmethod

from splice.core.entities.user import User


class UserRepositoryInterface(ABC):

    @abstractmethod
    async def salvar(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    async def deletar(self, user_id: int) -> None:
        raise NotImplementedError
