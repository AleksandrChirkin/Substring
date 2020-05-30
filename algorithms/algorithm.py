from abc import abstractmethod


class Algorithm:
    def __init__(self):
        pass

    @abstractmethod
    def run(self, text, template) -> int:
        raise NotImplementedError()
