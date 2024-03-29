from base64 import b64encode


class Binary:
    def __init__(self, number: str) -> None:
        self.num = number
        self.decimal
        self.hexadecimal
        self.octal
        self.ascii
        self.base64
        self.data = {"decimal": self.decimal, "hexadecimal": self.hexadecimal, "octal": self.octal, "ascii": self.ascii, "base64": self.base64}

    @property
    def decimal(self):
        return ' '.join(str(int(i, 2)) for i in self.num.split())

    @property
    def hexadecimal(self):
        return ' '.join(hex(int(i))[2:] for i in self.decimal.split()).upper()

    @property
    def octal(self):
        return ' '.join(oct(int(i))[2:] for i in self.decimal.split())

    @property
    def ascii(self):
        return ''.join(chr(int(i)) for i in self.decimal.split())

    @property
    def base64(self):
        return str(b64encode(bytes(self.ascii, 'utf-8')))[2:-1]
