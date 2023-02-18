from base64 import b64decode


class Base64:
    def __init__(self, text: str) -> None:
        self.text = text
        self.decimal
        self.binary
        self.hex
        self.octal
        self.ascii
        self.data = {"decimal": self.decimal, "binary": self.binary, "hex": self.hex, "octal": self.octal, "ascii": self.ascii}

    @property
    def decimal(self):
        return ' '.join(str(ord(i)) for i in self.ascii)

    @property
    def binary(self):
        return ' '.join(bin(int(i))[2:] for i in self.decimal.split())

    @property
    def hex(self):
        return ' '.join(hex(int(i))[2:] for i in self.decimal.split()).upper()

    @property
    def octal(self):
        return ' '.join(oct(int(i))[2:] for i in self.decimal.split())

    @property
    def ascii(self):
        return str(b64decode(bytes(self.text, 'utf-8')))[2:-1]
