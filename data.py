class Decimal:
    def __init__(self, num: int) -> None:
        self.num = num

    def to_binary(self) -> str:
        num = self.num
        result = ""

        if num == 0:
            result += "0"

        while num > 0:
            result += str(num % 2)
            num //= 2

        return result[::-1]

    def to_hex(self) -> str:
        return

    def to_octal(self) -> int:
        return


class Bianry:
    def __init__(self, num: str) -> None:
        self.num = num

    def to_deimal(self) -> int:
        return

    def to_hex(self) -> str:
        return

    def to_octal(self) -> int:
        return


class Hexadecimal:
    def __init__(self, num: str) -> None:
        self.num = num

    def to_deimal(self) -> int:
        return

    def to_binary(self) -> str:
        return

    def to_octal(self) -> int:
        return


class Octal:
    def __init__(self, num: int) -> None:
        self.num = num

    def to_deimal(self) -> int:
        return

    def to_binary(self) -> str:
        return

    def to_hex(self) -> str:
        return
