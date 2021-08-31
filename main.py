from data import *


def main() -> None:
    _type = str(input("""Write:
[1, D, Decimal]: To convert from Decimal
[2, B, Binary]: To convert from Binary
[3, H, Hex, Hexadecimal]: To convert from Hexadecimal
[4, O, Octal]: To convert from Octal
[5, E, Exit]: To Exit from the program
Choose one of this:\n""").strip()).capitalize()

    return check(_type)


def check(value: str) -> None:
    if value == "1" or value == "D" or value == "Decimal":
        return from_decimal(num=int(input("\nWrite a Decimal number:\n").strip()))

    elif value == "2" or value == "B" or value == "Binary":
        return from_binary(num=str(input("\nWrite a Binary number:\n").strip()))

    elif value == "3" or value == "H" or value == "Hex" or value == "Hexadecimal":
        return from_hex(num=str(input("\nWrite a Hexadecimal number:\n").strip()))

    elif value == "4" or value == "O" or value == "Octal":
        return from_octal(num=int(input("\nWrite a Octal number:\n").strip()))

    elif value == "5" or value == "E" or value == "Exit":
        exit()

    else:
        print("Wrong value please try again")
        return main()


def from_decimal(num: int) -> None:
    _num = Decimal(num)
    print(f"\nDecimal: {num}\nBinary: {_num.to_binary()}\nHexadecimal: {_num.to_hex()}\nOctal: {_num.to_octal()}\n")

    return main()


def from_binary(num: str) -> None:
    _num = Binary(num)
    print(f"\nBinary: {num}\nDecimal: {_num.to_decimal()}\nHexadecimal: {_num.to_hex()}\nOctal: {_num.to_octal()}\n")

    return main()


def from_hex(num: str) -> None:
    _num = Hexadecimal(num)
    print(f"\nHexadecimal: {num}\nDecimal: {_num.to_decimal()}\nBinary: {_num.to_binary()}\nOctal: {_num.to_octal()}\n")

    return main()


def from_octal(num: int) -> None:
    _num = Octal(num)
    print(f"\nOctal: {num}\nDecimal: {_num.to_decimal()}\nBinary: {_num.to_binary()}\nHexadecimal: {_num.to_hex()}\n")

    return main()


if __name__ == "__main__":
    main()
