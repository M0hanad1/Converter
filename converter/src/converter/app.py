"""
This app is using to convert between [Decimal, Binary, Hex, Octal, Ascii, Base64]
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from converter.data.decimal import Decimal
from converter.data.binary import Binary
from converter.data.hexadecimal import Hexadecimal
from converter.data.octal import Octal
from converter.data.ascii import Ascii
from converter.data.base64_ import Base64


class Converter(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, text_align="center", alignment="center"))

        text_label = toga.Label("Convert: ")
        self.number_input = toga.TextInput(placeholder="Write the number you want to convert from", style=Pack(flex=2, padding=(4)))

        text_label2 = toga.Label("From: ")
        self.mode = toga.Selection(items=["Decimal", "Binary", "Hexadecimal", "Octal", "Ascii", "Base64"], style=Pack(flex=2, padding=(4)))

        content_box1 = toga.Box(style=Pack(direction=ROW, padding=5, flex=3, text_align="center", alignment="center"))
        content_box1.add(text_label)
        content_box1.add(self.number_input)

        content_box2 = toga.Box(style=Pack(direction=ROW, padding=5, flex=3, text_align="center", alignment="center"))
        content_box2.add(text_label2)
        content_box2.add(self.mode)

        button = toga.Button("Convert", on_press=self.convert, style=Pack(padding=(7.5)))

        credits_box = toga.Box(style=Pack(alignment="bottom", padding=(50)))
        credits = toga.Label("Developer: Mohanad Ahmed", style=Pack(font_weight="bold"))
        credits_box.add(credits)


        main_box.add(content_box1)
        main_box.add(content_box2)
        main_box.add(button)
        main_box.add(credits_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def convert(self, _):
        value = self.mode.value
        number = self.number_input.value

        try:
            if value == "Decimal":
                convert_object = Decimal(number)

            elif value == "Binary":
                convert_object = Binary(number)

            elif value == "Hexadecimal":
                convert_object = Hexadecimal(number)

            elif value == "Octal":
                convert_object = Octal(number)

            elif value == "Ascii":
                convert_object = Ascii(number)

            else:
                convert_object = Base64(number)

        except:
            return self.main_window.error_dialog("Couldn't convert", "Wrong Value, please try again.")

        message = ""

        for key, value in convert_object.data.items():
            message += f"{key.capitalize()}: {value}\n\n"

        return self.main_window.info_dialog(f"Converted from: {self.mode.value}", message)


def main():
    return Converter()
