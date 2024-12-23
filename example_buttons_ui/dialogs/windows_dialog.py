from buttons.windows_button import WindowsButton
from dialogs.dialog import Dialog

class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()

