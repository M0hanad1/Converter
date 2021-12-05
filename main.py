from data import *


class Main:
    def __init__(self) -> None:
        self.num = ''

    def main(self) -> None:
        print(
            'Choose from these:\n[1, D, Decimal]: To convert from Decimal\n[2, B, Binary]: '
            'To convert from Binary\n[3, H, Hex, Hexadecimal]: To convert from Hexadecimal\n'
            '[4, O, Octal]: To convert from Octal\n[5, A, Ascii]: To convert from Ascii\n'
            '[6, B64, Base64]: To convert from Base64\n[7, E, Exit]: To exit from the program\n'
        )

        choose = input('Choose one of these:\n').replace(' ', '').upper()

        if choose == '7' or choose == 'E' or choose == 'EXIT':
            exit('\nSee you later')

        if choose == '1' or choose == 'D' or choose == 'DECIMAL':
            number = input('\nWrite the Decimal Number:\n')

        elif choose == '2' or choose == 'B' or choose == 'BINARY':
            number = input('\nWrite the binary number:\n')

        elif choose == '3' or choose == 'H' or choose == 'HEX' or choose == 'HEXADECIMAL':
            number = input('\nWrite the Hexadecimal number:\n')

        elif choose == '4' or choose == 'O' or choose == 'OCTAL':
            number = input('\nWrite the Octal number:\n')

        elif choose == '5' or choose == 'A' or choose == 'ASCII':
            number = input('\nWrite the ASCII number:\n')

        elif choose == '6' or choose == 'B64' or choose == 'BASE64':
            number = input('\nWrite the Base64 number:\n')

        else:
            print('\nWrong value please try again\n')
            return self.main()

    def from_decimal(self) -> None:
        x = Decimal(self.num)
        print(
            f'Decimal: {self.num}\n\nBinary: {x.to_binary()}\nHexadecimal: {x.to_hex()}\n'
            f'Octal: {x.to_octal}\nAscii: {x.to_ascii()}\nBase64: {x.to_base64()}'
        )

    def from_binary(self) -> None:
        x = Binary(self.num)
        print(
            f'Binary: {self.num}\n\nDecimal: {x.to_decimal()}\nHexadecimal: {x.to_hex()}\n'
            f'Octal: {x.to_octal}\nAscii: {x.to_ascii()}\nBase64: {x.to_base64()}'
        )

    def from_hex(self) -> None:
        x = Hexadecimal(self.num)
        print(
            f'Hexadecimal: {self.num}\n\nDecimal: {x.to_decimal()}\nBinary: {x.to_binary()}\n'
            f'Octal: {x.to_octal}\nAscii: {x.to_ascii()}\nBase64: {x.to_base64()}'
        )

    def from_octal(self) -> None:
        x = Octal(self.num)
        print(
            f'Octal: {self.num}\n\nDecimal: {x.to_decimal()}\nBinary: {x.to_binary()}\n'
            f'Hexadecimal: {x.to_hex()}\nAscii: {x.to_ascii()}\nBase64: {x.to_base64()}'
        )

    def from_ascii(self) -> None:
        x = Ascii(self.num)
        print(
            f'Ascii: {self.num}\n\nDecimal: {x.to_decimal()}\nBinary: {x.to_binary()}\n'
            f'Hexadecimal: {x.to_hex()}\nOctal: {x.to_octal()}\nBase64: {x.to_base64()}'
        )

    def from_base64(self) -> None:
        x = Base64_(self.num)
        print(
            f'Base64: {self.num}\n\nDecimal: {x.to_decimal()}\nBinary: {x.to_binary()}'
            f'\nHexadecimal: {x.to_hex()}\nOctal: {x.to_octal()}\nAscii: {x.to_ascii()}'
        )
