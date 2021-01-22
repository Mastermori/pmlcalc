from io import FileIO

from input_reader import InputReader
from string_reader import StringReader


class FileReader(InputReader):
    string_reader: InputReader

    def __init__(self, file_path: str):
        file = open(file_path, "r")
        file_str = file.read()
        self.string_reader = StringReader(file_str)

    def peek(self, k: int = 1):
        return self.string_reader.peek(k)

    def consume(self, k: int = 1):
        return self.string_reader.consume(k)

    def is_eof(self) -> bool:
        return self.string_reader.is_eof()
