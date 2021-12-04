from base64 import b64encode, b64decode


class Decimal:
    def __init__(self, number: str) -> None:
        self.num = number

    def to_binary(self) -> str:
        return ' '.join(bin(int(i))[2:] for i in self.num.split())

    def to_hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.num.split())

    def to_octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.num.split())

    def to_ascii(self) -> str:
        return ''.join(chr(int(i)) for i in self.num.split())

    def to_base64(self):
        return str(b64encode(bytes(self.to_ascii(), 'utf-8')))[2:-1]


class Binary:
    def __init__(self, number: str) -> None:
        self.num = number

        # if len(number.split()[0]) > 8:
        #     self.num = ''
        #     number = enumerate(number)

        #     for i, j in number:
        #         if (i / 8) - (i // 8) == 0:
        #             self.num += ' '

        #         self.num += j

    def to_decimal(self) -> str:
        return ' '.join(str(int(i, 2)) for i in self.num.split())

    def to_hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.to_decimal().split())

    def to_octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.to_decimal().split())

    def to_ascii(self) -> str:
        return ''.join(chr(int(i)) for i in self.to_decimal().split())

    def to_base64(self) -> str:
        return str(b64encode(bytes(self.to_ascii(), 'utf-8')))[2:-1]


class Hexadecimal:
    def __init__(self, number: str) -> None:
        self.num = number

    def to_decimal(self) -> str:
        return ' '.join(str(int(i, 16)) for i in self.num.split())

    def to_binary(self) -> str:
        return ' '.join(bin(int(i))[2:] for i in self.to_decimal().split())

    def to_octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.to_decimal().split())

    def to_ascii(self) -> str:
        return bytes.fromhex(self.num).decode('ASCII')

    def to_base64(self) -> str:
        return str(b64encode(bytes(self.to_ascii(), 'utf-8')))[2:-1]


class Octal:
    def __init__(self, num: str) -> None:
        self.num = num

    def to_decimal(self) -> str:
        return ' '.join(str(int(i, 8)) for i in self.num.split())

    def to_binary(self) -> str:
        return ' '.join(bin(int(i))[2:] for i in self.to_decimal().split())

    def to_hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.to_decimal().split())

    def to_ascii(self) -> str:
        return ''.join(chr(int(i)) for i in self.to_decimal().split())

    def to_base64(self) -> str:
        return str(b64encode(bytes(self.to_ascii(), 'utf-8')))[2:-1]


class Ascii:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_decimal(self) -> str:
        return ' '.join(str(ord(i)) for i in self.text)

    def to_binary(self) -> str:
        return ' '.join(bin(int(i))[2:] for i in self.to_decimal().split())

    def to_hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.to_decimal().split())

    def to_octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.to_decimal().split())

    def to_base64(self) -> str:
        return str(b64encode(bytes(self.text, 'utf-8')))[2:-1]


class Base64_:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_decimal(self) -> str:
        return ' '.join(str(ord(i)) for i in self.to_ascii())

    def to_binary(self) -> str:
        return ' '.join(bin(int(i))[2:] for i in self.to_decimal().split())

    def to_hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.to_decimal().split())

    def to_octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.to_decimal().split())

    def to_ascii(self) -> str:
        return str(b64decode(bytes(self.text, 'utf-8')))[2:-1]
