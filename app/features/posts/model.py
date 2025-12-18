from typing import Union
from dataclasses import dataclass, field
from datetime import date
import uuid

@dataclass
class Post:
    id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
    description: str
    created: date


class PostRepository:
    _elements: list[Post] = []

    def add(self, post: Post) -> Union[Exception, None]:
        self._elements.append(post)

    def remove(self, id: str) -> Union[Exception, None]:
        self._elements = list(filter(lambda ele: ele.id == id, self._elements))

    def list(self) -> Union[Exception, list[Post]]:
        return self._elements

    def get(self, id: str) -> Union[Exception, Post | None]:
        return filter(lambda ele: ele.id == id, self._elements)[0]
