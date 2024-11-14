# app/api/services/user_service.py
from splice.core.use_cases.user.atualizar_usuario import AtualizarUsuario
from splice.core.use_cases.user.buscar_usuario import BuscarUsuario
from splice.core.use_cases.user.criar_usuario import CriarUsuario
from splice.core.use_cases.user.deletar_usuario import DeletarUsuario
from splice.infra.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def criar_usuario(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        username: str,
        password: str,
        photo: str,
    ):
        caso_uso = CriarUsuario(self.repo)
        return await caso_uso.execute(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            username=username,
            password=password,
            photo=photo,
        )

    def buscar_usuario(self, user_id: int):
        caso_uso = BuscarUsuario(self.repo)
        return caso_uso.execute(user_id)

    def atualizar_usuario(
        self, user_id: int, nome: str = None, email: str = None
    ):
        caso_uso = AtualizarUsuario(self.repo)
        return caso_uso.execute(user_id=user_id, nome=nome, email=email)

    def deletar_usuario(self, user_id: int):
        caso_uso = DeletarUsuario(self.repo)
        return caso_uso.execute(user_id)
