from buttons.html_button import HTMLButton
from dialogs.dialog import Dialog

class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()

