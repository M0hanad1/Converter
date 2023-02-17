from base64 import b64encode


class Decimal:
    def __init__(self, number: str) -> None:
        self.num = number
        self.binary
        self.hex
        self.octal
        self.ascii
        self.base64

    @property
    def binary(self):
        return ' '.join(bin(int(i))[2:] for i in self.num.split())

    @property
    def hex(self):
        return ' '.join(hex(int(i))[2:] for i in self.num.split()).upper()

    @property
    def octal(self):
        return ' '.join(oct(int(i))[2:] for i in self.num.split())

    @property
    def ascii(self):
        return ''.join(chr(int(i)) for i in self.num.split())

    @property
    def base64(self):
        return str(b64encode(bytes(self.to_ascii(), 'utf-8')))[2:-1]
