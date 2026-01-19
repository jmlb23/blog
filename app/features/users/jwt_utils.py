from os import getenv
from datetime import datetime, timezone
import jwt


class TokenUtils:
    @staticmethod
    def create_token(user_id: str, user_name: str) -> str:
        token_params: dict[str, str] = {
            "id": user_id,
            "username": user_name,
            "exp": int(datetime.now(timezone.utc).timestamp() + 900)
        }
        return jwt.encode(
            payload=token_params,
            key=getenv("SECRET"),
            algorithm="HS256",
        )
