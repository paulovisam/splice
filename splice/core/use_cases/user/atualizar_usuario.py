# app/core/use_cases/atualizar_usuario.py
class AtualizarUsuario:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id: int, nome: str = None, email: str = None):
        usuario = self.user_repo.get_by_id(user_id)
        usuario.atualizar(nome=nome, email=email)
        self.user_repo.salvar(usuario)
        return usuario
