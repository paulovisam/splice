from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

from splice.core.models.user import User
from splice.infra.database import get_pg_session
from splice.infra.repositories.user_repository import UserRepository
from splice.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type: str


class AuthService:

    def __init__(self) -> None:
        # Chaves e algoritmos para o JWT
        self.SECRET_KEY = settings.JWT_SECRET_KEY
        self.ALGORITHM = settings.JWT_ALGORITHM
        self.ACCESS_TOKEN_EXPIRE_MINUTES = (
            settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.access_token_expires = timedelta(
            minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    async def authenticate_user(
        self, user_service, username: str, password: str
    ):
        user = await user_service.get_user_by_id(user_id=username)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    def create_access_token(self, data: dict) -> Token:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + self.access_token_expires
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM
        )
        return Token(access_token=encoded_jwt, token_type="bearer")

    # async def get_current_active_user(
    #     self,
    #     current_user: Annotated[User, Depends(get_current_user)],
    # ):
    #     if current_user.disabled:
    #         raise HTTPException(status_code=400, detail="Inactive user")
    #     return current_user


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db_session: Session = Depends(get_pg_session),
) -> User:
    repo = UserRepository(db_session)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica o token
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    # Recupera o usuário do banco de dados
    user = await repo.get_by_id(user_id)
    if user is None:
        raise credentials_exception

    return user
