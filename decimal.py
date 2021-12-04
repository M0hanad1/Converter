from base64 import b64encode


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
