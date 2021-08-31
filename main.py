from data import *


def main() -> None:
    _type = str(input("""Write:
[1, D, Decimal]: To convert from Decimal
[2, B, Binary]: To convert from Binary
[3, H, Hex, Hexadecimal]: To convert from Hexadecimal
[4, O, Octal]: To convert from Octal
[5, E, Exit]: To Exit from the program""").split()).capitalize()

    return check(_type)


def check(value: str) -> None:
    if value == "1" or value == "D" or value == "Decimal":
        pass

    elif value == "2" or value == "B" or value == "Binary":
        pass

    elif value == "3" or value == "H" or value == "Hex" or value == "Hexadecimal":
        pass

    elif value == "4" or value == "O" or value == "Octal":
        pass

    elif value == "5" or value == "E" or value == "Exit":
        exit()

    else:
        print("Wrong value please try again")
        return main()


if __name__ == "__main__":
    main()
