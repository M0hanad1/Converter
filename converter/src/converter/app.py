"""
This app is using to convert between [Decimal, Binary, Hex, Octal, Ascii, Base64]
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from converter.data.decimal import Decimal
from converter.data.binary import Binary
from converter.data.hexadecimal import Hexadecimal
from converter.data.octal import Octal
from converter.data.ascii import Ascii
from converter.data.base64_ import Base64


class Converter(toga.App):
    def __init__(self, formal_name=None, app_id=None, app_name=None, id=None, icon=None, author=None, version=None, home_page=None, description=None, startup=None, windows=None, on_exit=None, factory=None):
        self.language = "arabic"
        self.words = {
            "Convert": "تحويل",
            "From:": "من:",
            "Write the number you want to convert from": "أكتب العدد الذي تريد التحويل منه",
            "Decimal": "عشري",
            "Binary": "ثنائي",
            "Hexadecimal": "سداسي عشر",
            "Octal": "ثماني",
            "Ascii": "أسكي",
            "Base64": "الأساس 64",
            "Developer: Mohanad Ahmed": "المطور: مهند أحمد",
            "Couldn't convert": "لم يكتمل التحويل",
            "Wrong Value, please try again.": "مدخل خاطئ، بالرجاء المحاولة مجددا",
            "Converted from:": "تحويل من:",
            "Exit": "الخروج",
            "Choose Mode": "اختر الوضع",
            "Converter": "المحول",
            "Calculator": "الالة الحاسبة",
            "Calculate": "احسب",
            "Write the calculation you want to do": "اكتب العملية الحسابية التي تريد تنفيذها",
            "Type:": "النوع:",
            "Couldn't calc": "لم يتم الحساب",
            "There's no operation provided.": "لم يتم إضافة عملية حسابية",
            "Result": "الناتج",
            "Result from:": "الناتج من:"
        }
        super().__init__(formal_name, app_id, app_name, id, icon, author, version, home_page, description, startup, windows, on_exit, factory)

    def get_word(self, context):
        return context if self.language == "english" else self.words[context]

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN, text_align="center", alignment="center"))

        self.mainmenu()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def mainmenu(self):
        text_label = toga.Label(self.get_word("Choose Mode") + ":", style=Pack(text_align="center", alignment="center", padding_bottom=10))

        content_box = toga.Box(style=Pack(direction=COLUMN, padding=5, text_align="center", alignment="center"))
        content_box.add(text_label)

        convert_mode_button = toga.Button(self.get_word("Converter"), on_press=self.change_mode, id="convert", style=Pack(padding=(7.5)))

        calc_mode_button = toga.Button(self.get_word("Calculator"), on_press=self.change_mode, id="calc", style=Pack(padding=(7.5)))

        credits_box = toga.Box(style=Pack(alignment="bottom", padding=(50)))
        credits = toga.Label(self.get_word("Developer: Mohanad Ahmed"), style=Pack(font_weight="bold"))
        credits_box.add(credits)

        self.main_box.add(content_box)
        self.main_box.add(convert_mode_button)
        self.main_box.add(calc_mode_button)
        self.main_box.add(credits_box)

    def converter(self):
        text_label = toga.Label(self.get_word("Convert") + ":", style=Pack(text_align="center", alignment="center", padding_bottom=10))
        self.number_input = toga.TextInput(placeholder=self.get_word("Write the number you want to convert from"), style=Pack(flex=2, padding=(4)))

        text_label2 = toga.Label(self.get_word("From:"), style=Pack(text_align="center", alignment="center", padding_bottom=10))
        self.mode = toga.Selection(items=[
            self.get_word("Decimal"),
            self.get_word("Binary"),
            self.get_word("Hexadecimal"),
            self.get_word("Octal"),
            self.get_word("Ascii"),
            self.get_word("Base64")
        ], style=Pack(flex=2, padding=(4), padding_bottom=10))

        content_box1 = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=3, text_align="center", alignment="center"))
        content_box1.add(text_label)
        content_box1.add(self.number_input)

        content_box2 = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=3, text_align="center", alignment="center"))
        content_box2.add(text_label2)
        content_box2.add(self.mode)

        convert_button = toga.Button(self.get_word("Convert"), on_press=self.convert, style=Pack(padding=(7.5)))

        exit_button = toga.Button(self.get_word("Exit"), on_press=self.change_mode, style=Pack(padding=(7.5)))

        credits_box = toga.Box(style=Pack(alignment="bottom", padding=(50)))
        credits = toga.Label(self.get_word("Developer: Mohanad Ahmed"), style=Pack(font_weight="bold"))
        credits_box.add(credits)

        self.main_box.add(content_box1)
        self.main_box.add(content_box2)
        self.main_box.add(convert_button)
        self.main_box.add(exit_button)
        self.main_box.add(credits_box)

    def convert(self, _):
        value = self.mode.value
        number = self.number_input.value

        try:
            if len(number.replace(" ", "")) == 0:
                raise

            if value == self.get_word("Decimal"):
                convert_object = Decimal(number)

            elif value in self.get_word("Binary"):
                convert_object = Binary(number)

            elif value in self.get_word("Hexadecimal"):
                convert_object = Hexadecimal(number)

            elif value in self.get_word("Octal"):
                convert_object = Octal(number)

            elif value in self.get_word("Ascii"):
                convert_object = Ascii(number)

            else:
                convert_object = Base64(number)

        except:
            return self.main_window.error_dialog(self.get_word("Couldn't convert"), self.get_word("Wrong Value, please try again."))

        message = ""

        for key, value in convert_object.data.items():
            message += f"{self.get_word(key.capitalize())}:\n{value}\n\n"

        return self.main_window.info_dialog(f"{self.get_word('Converted from:')} {self.mode.value}", message)

    def change_mode(self, button):
        self.main_box.remove(*self.main_box.children)

        if button.id == "convert":
            return self.converter()
        
        if button.id == "calc":
            return self.calc()

        return self.mainmenu()

    def calc(self):
        text_label1 = toga.Label(self.get_word("Calculate") + ":", style=Pack(text_align="center", alignment="center", padding_bottom=10))
        self.number_input = toga.TextInput(placeholder=self.get_word("Write the calculation you want to do"), style=Pack(flex=2, padding=(4)))

        text_label2 = toga.Label(self.get_word("Type:"), style=Pack(text_align="center", alignment="center", padding_bottom=10))
        self.mode = toga.Selection(items=[
            self.get_word("Decimal"),
            self.get_word("Binary"),
            self.get_word("Octal"),
            self.get_word("Hexadecimal")
        ], style=Pack(flex=2, padding=(4), padding_bottom=10))

        text_label3 = toga.Label(self.get_word("Result") + ":", style=Pack(text_align="center", alignment="center", padding_bottom=10))
        self.result = toga.TextInput(value="0", readonly=True, style=Pack(flex=2, padding=(4)))

        content_box1 = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=3, text_align="center", alignment="center"))
        content_box1.add(text_label1)
        content_box1.add(self.number_input)

        content_box2 = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=3, text_align="center", alignment="center"))
        content_box2.add(text_label2)
        content_box2.add(self.mode)

        content_box3 = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=3, text_align="center", alignment="center"))
        content_box3.add(text_label3)
        content_box3.add(self.result)

        convert_button = toga.Button(self.get_word("Calculate"), on_press=self.calc_logic, style=Pack(padding=(7.5)))

        exit_button = toga.Button(self.get_word("Exit"), on_press=self.change_mode, style=Pack(padding=(7.5)))

        credits_box = toga.Box(style=Pack(alignment="bottom", padding=(50)))
        credits = toga.Label(self.get_word("Developer: Mohanad Ahmed"), style=Pack(font_weight="bold"))
        credits_box.add(credits)

        self.main_box.add(content_box1)
        self.main_box.add(content_box2)
        self.main_box.add(content_box3)
        self.main_box.add(convert_button)
        self.main_box.add(exit_button)
        self.main_box.add(credits_box)

    def calc_logic(self, _):
        calc = self.number_input.value.lower().replace(" ", "").replace("x", "*").replace("×", "*").replace("÷", "/").replace("/", "//").replace("^", "**")
        value = self.mode.value
        number = ""
        numbers = []
        ope = []
        index = 0

        try:
            for i in calc:
                if i in ["+", "-", "/", "*", "(", ")"]:
                    ope.append(i)
                    numbers.append(number)
                    number = ""
                    continue

                number += i

            if len(ope) == 0:
                return self.main_window.error_dialog(self.get_word("Couldn't calc"), self.get_word("There's no operation provided."))

            numbers.append(number)
            number = ""

            for i in numbers:
                if value == self.get_word("Decimal"):
                    convert_object = Decimal(i).num
                    type_ = "num"

                elif value in self.get_word("Binary"):
                    convert_object = Binary(i).decimal
                    type_ = "binary"

                elif value in self.get_word("Hexadecimal"):
                    convert_object = Hexadecimal(i).decimal
                    type_ = "hexadecimal"

                else:
                    convert_object = Octal(i).decimal
                    type_ = "octal"

                number +=  convert_object

                if index < len(ope):
                    number += ope[index]
                    index += 1

            result = (getattr(Decimal(str(eval(number))), type_))
            self.result.value = result
            return self.main_window.info_dialog(f"{self.get_word('Result from:')} {self.mode.value}", result)

        except:
            return self.main_window.error_dialog(self.get_word("Couldn't calc"), self.get_word("Wrong Value, please try again."))


def main():
    return Converter()
