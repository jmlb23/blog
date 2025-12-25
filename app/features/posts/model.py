from typing import Union
from dataclasses import dataclass, field
from datetime import date
import uuid
from abc import ABC, abstractmethod


@dataclass
class Post:
    id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
    description: str
    created: date


class AbstractPostRepository(ABC):
    @abstractmethod
    def add(self, post: Post) -> Union[Exception, str]:
        pass

    @abstractmethod
    def remove(self, id: str) -> Union[Exception, None]:
        pass

    @abstractmethod
    def list(self) -> Union[Exception, list[Post]]:
        pass

    @abstractmethod
    def get(self, id: str) -> Union[Exception, Post | None]:
        pass


class PostRepository(AbstractPostRepository):
    _elements: list[Post] = []

    def add(self, post: Post) -> Union[Exception, str]:
        self._elements.append(post)
        return post.id

    def remove(self, id: str) -> Union[Exception, None]:
        self._elements = list(filter(lambda ele: ele.id == id, self._elements))

    def list(self) -> Union[Exception, list[Post]]:
        return self._elements

    def get(self, id: str) -> Union[Exception, Post | None]:
        return list(filter(lambda ele: ele.id == id, self._elements))[0]


def get_repo() -> AbstractPostRepository:
    return PostRepository()
