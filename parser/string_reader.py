from input_reader import InputReader


class StringReader(InputReader):
    string_list: list

    def __init__(self, string: str):
        self.string_list = list(string)

    def is_eof(self) -> bool:
        return len(self.string_list) == 0

    def peek(self, k: int = 0):
        return self.string_list[k]

    def consume(self, k: int = 0):
        c: chr = self.string_list[k]
        del self.string_list[k]
        return c
