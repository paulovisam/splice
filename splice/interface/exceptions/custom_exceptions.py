from fastapi import HTTPException


class AcessoNegado(HTTPException):
    def __init__(self, detail: str = 'Acesso negado'):
        super().__init__(status_code=403, detail=detail)


class NotFoundException(Exception):
    def __init__(self, detail: str = 'Resource not found'):
        self.detail = detail


class BusinessException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class ValidationException(Exception):
    def __init__(self, detail: str):
        self.detail = detail
