class Hexadecimal:
    def __init__(self, number: str) -> None:
        self.num = number

    def to_decimal(self) -> int:
        return int(self.num, 16)

    def to_binary(self) -> str:
        return bin(self.to_decimal())[2:]

    def to_octal(self) -> str:
        return oct(self.to_decimal())[2:]

    def to_ascii(self) -> str:
        return bytes.fromhex(self.num).decode('ASCII')


bt = Hexadecimal('482045')
print(bt.to_decimal())
print(bt.to_hex())
print(bt.to_ascii())
print(bt.to_octal())
print(bt.to_base64())
