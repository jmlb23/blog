from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Union
import uuid
import bcrypt


@dataclass
class User:
    id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
    user_name: str
    password: str


class AbstractUserRepository(ABC):
    @abstractmethod
    def auth(
            self,
            user_name: str,
            password: str
    ) -> Union[Exception, User | None]:
        pass


class UserRepository(AbstractUserRepository):
    users: list[User] = [
        User(
            user_name="jmlb23",
            password="$2b$14$aGXqCIU1j4x6lSYYJyoE5u93OhdcQiDh6uulaMCmM4bxtO6AWB87e"
        )
    ]

    def auth(
            self,
            user_name: str,
            password: str
    ) -> Union[Exception, str | None]:
        return list(
            filter(lambda u:
                   u.user_name == user_name and
                   bcrypt.checkpw(password.encode(), u.password.encode()),
                   self.users)
        )[0]


def get_repo() -> AbstractUserRepository:
    return UserRepository()
