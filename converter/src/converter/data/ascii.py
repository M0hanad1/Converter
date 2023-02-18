from base64 import b64encode


class Ascii:
    def __init__(self, text: str) -> None:
        self.text = text
        self.decimal
        self.binary
        self.hex
        self.octal
        self.base64
        self.data = {"decimal": self.decimal, "binary": self.binary, "hex": self.hex, "octal": self.octal, "base64": self.base64}

    @property
    def decimal(self) -> str:
        return ' '.join(str(ord(i)) for i in self.text)

    @property
    def binary(self) -> str:
        return ' '.join(bin(int(i))[2:] for i in self.decimal.split())

    @property
    def hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.decimal.split()).upper()

    @property
    def octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.decimal.split())

    @property
    def base64(self) -> str:
        return str(b64encode(bytes(self.text, 'utf-8')))[2:-1]
