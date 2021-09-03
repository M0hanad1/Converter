class functions:
    global check

    def check(result: str) -> str:
        for i in result:
            if i == "0":
                result = result[1:]
            else:
                break

        return result


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
                result += _hex[num % 16]

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
        result = 0
        pow_num = 0

        for i in self.num[::-1]:
            result += int(i) * pow(2, pow_num)
            pow_num += 1

        return result

    def to_hex(self) -> str:
        num = self.num
        _hex = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"
        }
        nums = {}
        index = 0
        nums_value = 0
        result = ""

        while (len(num) / 4) - (len(num) // 4) != 0:
            num = "0" + num

        while len(num) != 0:
            for i in range(0, 4):
                if i == 0:
                    nums[nums_value] = num[0]

                else:
                    nums[nums_value] += num[index]

                index += 1

            nums_value += 1
            num = num[index:]
            index = 0

        for i in nums:
            result += _hex[nums[i]]

        return check(result)

    def to_octal(self) -> str:
        num = self.num
        result = ""
        nums = {}
        index = 0
        nums_value = 0
        multi_num = 1
        result_num = 0

        while (len(num) / 3) - (len(num) // 3) != 0:
            num = "0" + num

        while len(num) > 0:
            for i in range(0, 3):
                if i == 0:
                    nums[nums_value] = num[index]

                else:
                    nums[nums_value] += num[index]

                index += 1

            nums_value += 1
            num = num[index:]
            index = 0

        for i in nums:
            b_num = nums[i]

            for j in b_num[::-1]:
                result_num += int(j) * multi_num
                multi_num *= 2

            multi_num = 1
            result += str(result_num)
            result_num = 0

        return check(result)


class Hexadecimal:
    def __init__(self, num: str) -> None:
        self.num = num

    def to_decimal(self) -> int:
        _hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        result = 0
        pow_num = 0

        for i in self.num[::-1]:
            if i in _hex:
                result += _hex[i] * pow(16, pow_num)

            else:
                result += int(i) * pow(16, pow_num)

            pow_num += 1

        return result

    def to_binary(self) -> str:
        _hex = {
            "0": "0000", "1": "0001", "2": "0010", "3": '0011', "4": "0100", "5": "0101", "6": "0110", "7": "0111",
            "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"
        }
        result = ""

        for i in check(self.num):
            result += _hex[i]

        return result

    def to_octal(self) -> str:
        return Binary(self.to_binary()).to_octal()


class Octal:
    def __init__(self, num: int) -> None:
        self.num = num

    def to_decimal(self) -> int:
        result = 0
        pow_num = 0

        for i in str(self.num)[::-1]:
            result += int(i) * pow(8, pow_num)
            pow_num += 1

        return result

    def to_binary(self) -> str:
        result = ""
        binary = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}

        for i in str(self.num):
            result += binary[int(i)]

        return check(result)

    def to_hex(self) -> str:
        return Binary(self.to_binary()).to_hex()
