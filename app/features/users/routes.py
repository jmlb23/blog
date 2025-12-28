from fastapi import APIRouter, Depends
from .dto import LoginDTO, LoginResponseDTO
from .jwt_utils import TokenUtils
from typing import Annotated
from .model import AbstractUserRepository, get_repo

userRouter = APIRouter()


@userRouter.post("/login")
def login(
    login: LoginDTO,
    repo: Annotated[AbstractUserRepository, Depends(get_repo)]
) -> LoginResponseDTO | None:
    if user_id := repo.auth(login.username, login.password) is not None:
        return LoginResponseDTO(
            token=TokenUtils.create_token(user_id, login.username)
        )
    else:
        return None
