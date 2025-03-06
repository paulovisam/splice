from typing import Annotated

from fastapi import APIRouter, Depends, status

# from splice.app import app
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from splice.infra.database import get_pg_session
from splice.interface.service.auth_service import AuthService, Token
from splice.interface.service.user_service import UserRepository, UserService

router = APIRouter(prefix='/auth')


@router.post("/token")
async def get_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db_session: Session = Depends(get_pg_session),
) -> Token:
    repo_user = UserRepository(db_session)
    user_service = UserService(repo_user)
    service = AuthService()
    user = await service.authenticate_user(
        user_service=user_service,
        username=form_data.username,
        password=form_data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return service.create_access_token(data={"sub": str(user.id)})
