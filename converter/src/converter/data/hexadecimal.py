from base64 import b64encode


class Hexadecimal:
    def __init__(self, number: str) -> None:
        self.num = number
        self.decimal
        self.binary
        self.octal
        self.ascii
        self.base64
        self.data = {"decimal": self.decimal, "binary": self.binary, "octal": self.octal, "ascii": self.ascii, "base64": self.base64}

    @property
    def decimal(self):
        return ' '.join(str(int(i, 16)) for i in self.num.split())

    @property
    def binary(self):
        return ' '.join(bin(int(i))[2:] for i in self.decimal.split())

    @property
    def octal(self):
        return ' '.join(oct(int(i))[2:] for i in self.decimal.split())

    @property
    def ascii(self):
        return ''.join(chr(int(i)) for i in self.decimal.split())

    @property
    def base64(self):
        return str(b64encode(bytes(self.ascii, 'utf-8')))[2:-1]
