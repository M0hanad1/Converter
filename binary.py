import base64


class Binary:
    def __init__(self, number: str) -> None:
        self.num = number

        if len(number.split()[0]) > 8:
            self.num = ''
            number = enumerate(number)

            for i, j in number:
                if (i / 8) - (i // 8) == 0:
                    self.num += ' '

                self.num += j

    def to_decimal(self) -> str:
        return ' '.join(str(int(i, 2)) for i in self.num.split())

    def to_hex(self) -> str:
        return ' '.join(hex(int(i))[2:] for i in self.to_decimal().split())

    def to_octal(self) -> str:
        return ' '.join(oct(int(i))[2:] for i in self.to_decimal().split())

    def to_base64(self) -> str:
        return str(base64.b64encode(bytes(self.to_ascii(), 'utf-8')))[2:-1]

    def to_ascii(self) -> str:
        return ''.join(chr(int(i)) for i in self.to_decimal().split())
