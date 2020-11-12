from abc import abstractmethod
from typing import Any


class Algorithm:
    @abstractmethod
    def run(self, text: Any, template: str) -> int:
        raise NotImplementedError()
