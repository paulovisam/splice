# app/core/use_cases/deletar_usuario.py
class DeletarUsuario:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id: int):
        self.user_repo.deletar(user_id)
