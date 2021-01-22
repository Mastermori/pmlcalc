from abc import ABC, abstractmethod


class Consumer(ABC):
    k: int

    @abstractmethod
    def peek(self, k: int = 0):
        k = k
        pass

    @abstractmethod
    def consume(self, k: int = 0):
        pass
