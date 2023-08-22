from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.clipboard import Clipboard
from kivy.uix.textinput import TextInput
import CRT

class StyledTextInput(TextInput):
    halign='center'
    valign='middle'


class Root(GridLayout):
    def main_encrypt_copy(self):
        self.ids.label1.text = CRT.create_crypt_sentence(self.ids.input1.text)
        Clipboard.copy(self.ids.label1.text)
    def main_decrypt(self):
        self.ids.label1.text = CRT.decrypt(self.ids.input1.text)
    def on_text_validate(self, instance):
        self.ids.input1.focus = False



class CryptApp(App):
    title = 'CheatRSA.app'
    icon = 'penguin_icon1.png'


if __name__ == '__main__':
    CryptApp().run()