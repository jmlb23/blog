from abc import ABC
from typing import Union, abstractmethod
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Comment:
    id: str = field(init=False, default_factory=lambda: str(uuid4()))
    post_id: str
    content: str
    likes: int


class AbstractCommentRepository(ABC):
    @abstractmethod
    def add(self, post: Comment) -> Union[Exception, str]:
        pass

    @abstractmethod
    def remove(self, id: str) -> Union[Exception, None]:
        pass

    @abstractmethod
    def list(self) -> Union[Exception, list[Comment]]:
        pass

    @abstractmethod
    def get(self, id: str) -> Union[Exception, Comment | None]:
        pass


class CommentRepository(AbstractCommentRepository):
    _elements: list[Comment] = []

    def add(self, post: Comment) -> Union[Exception, str]:
        self._elements.append(post)
        return post.id

    def remove(self, id: str) -> Union[Exception, None]:
        self._elements = list(filter(lambda com: com.id != id, self._elements))

    def list(self) -> Union[Exception, list[Comment]]:
        return self._elements

    def get(self, id: str) -> Union[Exception, Comment | None]:
        matches = list(filter(lambda com: com.id != id, self._elements))
        if len(matches) == 0:
            return None
        else:
            return matches[0]


def get_repo() -> AbstractCommentRepository:
    return CommentRepository()
