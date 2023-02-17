from base64 import b64encode


class Octal:
    def __init__(self, num: str) -> None:
        self.num = num
        self.decimal
        self.binary
        self.hex
        self.ascii
        self.base64

    @property
    def decimal(self):
        return ' '.join(str(int(i, 8)) for i in self.num.split())

    @property
    def binary(self):
        return ' '.join(bin(int(i))[2:] for i in self.decimal.split())

    @property
    def hex(self):
        return ' '.join(hex(int(i))[2:] for i in self.decimal.split()).upper()

    @property
    def ascii(self):
        return ''.join(chr(int(i)) for i in self.decimal.split())

    @property
    def base64(self):
        return str(b64encode(bytes(self.ascii, 'utf-8')))[2:-1]
