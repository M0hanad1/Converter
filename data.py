class Decimal:
    def __init__(self, num: int) -> None:
        self.num = num

    def to_binary(self) -> str:
        num = self.num
        result = ""

        if num == 0:
            result += "0"

        while num > 0:
            result += str(num % 2)
            num //= 2

        return result[::-1]

    def to_hex(self) -> str:
        num = self.num
        _hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        result = ""

        if num == 0:
            result += "0"

        while num > 0:
            if num % 16 in _hex:
                result += _hex[num]

            else:
                result += str(num % 16)

            num //= 16

        return result[::-1]

    def to_octal(self) -> str:
        num = self.num
        result = ""

        if num == 0:
            pass

        while num > 0:
            if num % 8 > 7:
                result += "7"

            else:
                result += str(num % 8)

            num //= 8

        return result[::-1]


class Binary:
    def __init__(self, num: str) -> None:
        self.num = num

    def to_decimal(self) -> int:
        num = self.num
        result = 0
        pow_num = 0

        for i in num[::-1]:
            result += int(i) * pow(2, pow_num)
            pow_num += 1

        return result

    def to_hex(self) -> str:
        num = self.num
        _hex = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6","0111": "7", 
            "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"
        }
        nums = {}
        index = 0
        nums_value = 0
        result = ""

        if (len(num) / 4) - (len(num) // 4) == 0:
            pass

        else:
            while (len(num) / 4) - (len(num) // 4) != 0:
                num = "0" + num

        while len(num) != 0:
            for i in range(0, 4):
                if i == 0:
                    nums[nums_value] = num[0]
                else:
                    nums[nums_value] = nums[nums_value] + num[index]
                index += 1
            nums_value += 1
            num = num[index:]
            index = 0

        for i in nums:
            result += _hex[nums[i]]

        return result

    def to_octal(self) -> int:
        return


class Hexadecimal:
    def __init__(self, num: str) -> None:
        self.num = num

    def to_decimal(self) -> int:
        return

    def to_binary(self) -> str:
        return

    def to_octal(self) -> int:
        return


class Octal:
    def __init__(self, num: int) -> None:
        self.num = num

    def to_decimal(self) -> int:
        return

    def to_binary(self) -> str:
        return

    def to_hex(self) -> str:
        return


bina = Binary("1011")
print(bina.to_decimal())
print(bina.to_hex())
print(bina.to_octal())
