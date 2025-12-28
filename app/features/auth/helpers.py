from os import getenv
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from typing import Annotated, Any
from fastapi import Depends
import jwt

bearer_scheme = HTTPBearer()


def get_current_user(
    token: Annotated[str, Depends(bearer_scheme)]
) -> dict[str, Any]:
    try:
        return jwt.decode(token, getenv("SECRET"), algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, headers={
                            "WWW-Authenticate": "Bearer"})
