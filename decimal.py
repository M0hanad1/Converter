from typing import Union


class Decimal:
    def __init__(self, number: Union[int, str]) -> None:
        self.num = number

    def to_binary(self) -> str:
        return bin(self.num)[2:]

    def to_hex(self) -> str:
        return hex(self.num)[2:]

    def to_octal(self) -> str:
        return oct(self.num)[2:]

    def to_ascii(self) -> str:
        return ''.join(chr(int(i)) for i in self.num.split())
