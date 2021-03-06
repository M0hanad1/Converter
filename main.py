from binascii import Error
from data import *


class Main:
    def __init__(self) -> None:
        self.num = ''

    def main(self) -> None:
        print(
            'Choose from these:\n[1, D, Decimal]: To convert from Decimal\n[2, B, Binary]: '
            'To convert from Binary\n[3, H, Hex, Hexadecimal]: To convert from Hexadecimal\n'
            '[4, O, Octal]: To convert from Octal\n[5, A, Ascii]: To convert from Ascii\n'
            '[6, 64, B64, Base64]: To convert from Base64\n[7, E, Exit]: To exit from the program\n'
        )

        try:
            return self.run()

        except (Error, ValueError):
            print('\nWrong value please try again\n')

        except OverflowError:
            print('Ascii: Unable to convert\nBase64: Unable to convert\n')

        return self.main()

    def run(self) -> None:
        choose = input('Choose one of these:\n').replace(' ', '').upper()

        if choose == '7' or choose == 'E' or choose == 'EXIT':
            exit('\nSee you later')

        if choose == '1' or choose == 'D' or choose == 'DECIMAL':
            number = input('\nWrite the Decimal Number:\n')

            if len(number.replace(' ', '')) < 1:
                print('\nWrong value please try again\n')
                return self.main()

            self.num = number
            return self.from_decimal()

        elif choose == '2' or choose == 'B' or choose == 'BINARY':
            number = input('\nWrite the binary number:\n')

            if len(number.replace(' ', '')) < 1:
                print('\nWrong value please try again\n')
                return self.main()

            self.num = number
            return self.from_binary()

        elif choose == '3' or choose == 'H' or choose == 'HEX' or choose == 'HEXADECIMAL':
            number = input('\nWrite the Hexadecimal number:\n').lower()

            if len(number.replace(' ', '')) < 1:
                print('\nWrong value please try again\n')
                return self.main()

            self.num = number
            return self.from_hex()

        elif choose == '4' or choose == 'O' or choose == 'OCTAL':
            number = input('\nWrite the Octal number:\n')

            if len(number.replace(' ', '')) < 1:
                print('\nWrong value please try again\n')
                return self.main()

            self.num = number
            return self.from_octal()

        elif choose == '5' or choose == 'A' or choose == 'ASCII':
            number = input('\nWrite the ASCII number:\n')

            if len(number.replace(' ', '')) < 1:
                print('\nWrong value please try again\n')
                return self.main()

            self.num = number
            return self.from_ascii()

        elif choose == '6' or choose == '64' or choose == 'B64' or choose == 'BASE64':
            number = input('\nWrite the Base64 number:\n')

            if len(number.replace(' ', '')) < 1:
                print('\nWrong value please try again\n')
                return self.main()

            self.num = number
            return self.from_base64()

        else:
            print('\nWrong value please try again\n')
            return self.main()

    def from_decimal(self) -> None:
        x = Decimal(self.num)

        print(
            f'\nDecimal: {self.num}\n\nBinary: {x.to_binary()}\n'
            f'Hexadecimal: {x.to_hex()}\nOctal: {x.to_octal()}'
        )
        print(f'Ascii: {x.to_ascii()}\nBase64: {x.to_base64()}\n')

        return self.main()

    def from_binary(self) -> None:
        x = Binary(self.num)

        print(
            f'\nBinary: {self.num}\n\nDecimal: {x.to_decimal()}\n'
            f'Hexadecimal: {x.to_hex()}\nOctal: {x.to_octal()}'
        )
        print(f'Ascii: {x.to_ascii()}\nBase64: {x.to_base64()}\n')

        return self.main()

    def from_hex(self) -> None:
        x = Hexadecimal(self.num)

        print(
            f'\nHexadecimal: {self.num}\n\nDecimal: {x.to_decimal()}'
            f'\nBinary: {x.to_binary()}\nOctal: {x.to_octal()}'
        )
        print(f'Ascii: {x.to_ascii()}\nBase64: {x.to_base64()}\n')

        return self.main()

    def from_octal(self) -> None:
        x = Octal(self.num)

        print(
            f'\nOctal: {self.num}\n\nDecimal: {x.to_decimal()}\n'
            f'Binary: {x.to_binary()}\nHexadecimal: {x.to_hex()}'
        )

        try:
            print(f'Ascii: {x.to_ascii()}\nBase64: {x.to_base64()}\n')

        except ValueError:
            print('Ascii: Unable to convert\nBase64: Unable to convert\n')

        return self.main()

    def from_ascii(self) -> None:
        x = Ascii(self.num)

        print(
            f'\nAscii: {self.num}\n\nDecimal: {x.to_decimal()}\n'
            f'Binary: {x.to_binary()}\nHexadecimal: {x.to_hex()}\n'
            f'Octal: {x.to_octal()}\nBase64: {x.to_base64()}\n'
        )

        return self.main()

    def from_base64(self) -> None:
        x = Base64_(self.num)

        print(
            f'\nBase64: {self.num}\n\nDecimal: {x.to_decimal()}\n'
            f'Binary: {x.to_binary()}\nHexadecimal: {x.to_hex()}'
            f'\nOctal: {x.to_octal()}\nAscii: {x.to_ascii()}\n'
        )

        return self.main()
