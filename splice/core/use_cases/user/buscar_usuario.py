# app/core/use_cases/buscar_usuario.py
class BuscarUsuario:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id: int):
        return self.user_repo.get_by_id(user_id)
