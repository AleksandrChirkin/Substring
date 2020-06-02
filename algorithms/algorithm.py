from abc import abstractmethod


class Algorithm:
    @abstractmethod
    def run(self, text, template) -> int:
        raise NotImplementedError()
