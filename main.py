from data import *
from sys import exit


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
        return from_decimal(input("\nWrite a Decimal number:\n").strip())

    elif value == "2" or value == "B" or value == "Binary":
        return from_binary(input("\nWrite a Binary number:\n").strip())

    elif value == "3" or value == "H" or value == "Hex" or value == "Hexadecimal":
        return from_hex(input("\nWrite a Hexadecimal number:\n").strip().upper())

    elif value == "4" or value == "O" or value == "Octal":
        return from_octal(input("\nWrite a Octal number:\n").strip())

    elif value == "5" or value == "E" or value == "Exit":
        exit("Okay, see you later")

    else:
        print("\nWrong value please try again\n")
        return main()


def from_decimal(num: str) -> None:
    try:
        int(num)

    except ValueError or TypeError:
        if len(num) == 0:
            print("\nYou have to write the Decimal number, please try again\n")

        else:
            print(f"\n{num} is not a Decimal number, please try again\n")

        main()

    _num = Decimal(int(num))
    print(f"\nDecimal: {num}\nBinary: {_num.to_binary()}\nHexadecimal: {_num.to_hex()}\nOctal: {_num.to_octal()}\n")

    return main()


def from_binary(num: str) -> None:
    _num = Binary(num)

    if len(num) == 0:
        print("\nYou have to write the Binary number, please try again\n")

    else:
        if _num.check is False:
            print(f"\n{num} is not a Binary number, please try again\n")

        else:
            print(f"\nBinary: {num}\nDecimal: {_num.to_decimal()}\nHexadecimal: {_num.to_hex()}\n"
                  f"Octal: {_num.to_octal()}\n")

    return main()


def from_hex(num: str) -> None:
    _num = Hexadecimal(num)

    if len(num) == 0:
        print("\nYou have to write the Hexadecimal number, please try again\n")

    else:
        if _num.check is False:
            print(f"\n{num} is not a Hexadecimal number, please try again\n")

        else:
            print(f"\nHexadecimal: {num}\nDecimal: {_num.to_decimal()}\nBinary: {_num.to_binary()}\n"
                  f"Octal: {_num.to_octal()}\n")

    return main()


def from_octal(num: str) -> None:
    try:
        int(num)

    except ValueError or TypeError:
        if len(num) == 0:
            print("\nYou have to write the Octal number, please try again\n")

        else:
            print(f"\n{num} is not a Octal number, please try again\n")

        main()

    _num = Octal(int(num))

    if _num.check is False:
        print(f"\n{num} is not a Octal number, please try again\n")

    else:
        print(f"\nOctal: {num}\nDecimal: {_num.to_decimal()}\nBinary: {_num.to_binary()}\n"
              f"Hexadecimal: {_num.to_hex()}\n")

    return main()
