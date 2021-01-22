from abc import ABC, abstractmethod

from consumer import Consumer


class InputReader(Consumer, ABC):

    @abstractmethod
    def is_eof(self) -> bool:
        pass
