from abc import ABC, abstractmethod


class AbstractSpamFilter(ABC):
    def __init__(self, string: str):
        self.string = string

    @abstractmethod
    def filter(self) -> bool:
        raise NotImplementedError
