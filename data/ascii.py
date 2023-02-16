from base64 import b64encode


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
