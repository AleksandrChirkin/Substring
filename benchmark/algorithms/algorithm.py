from abc import abstractmethod
from io import StringIO, TextIOWrapper
from typing import Iterable, Union


class Algorithm:
    @abstractmethod
    def run(self, text: Union[StringIO, TextIOWrapper],
            template: str, number: int) -> Iterable[int]:
        raise NotImplementedError
