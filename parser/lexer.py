from parser.consumer import Consumer
from input_reader import InputReader


class Lexer(Consumer):

    reader: InputReader

    def __init__(self, reader: InputReader):
        self.reader = reader

    def peek(self, k: int = 0):
        pass

    def consume(self, k: int = 0):
        pass
