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
            password="$2a$12$HfEM2moO1TFcif/2wDE9KeCKXp.f5x01/fPrwLWLgyprW.C9ZmoVC"
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
                   bcrypt.checkpw(password.encode("UTF-8"),
                                  u.password.encode("UTF-8")),
                   self.users)
        )[0]


def get_repo() -> AbstractUserRepository:
    return UserRepository()
