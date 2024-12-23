from buttons.interfaces.button import Button

class WindowsButton(Button):
    def render(self):
        print("Render : Bouton au style Windows.")

    def on_click(self, function):
        print("WindowsButton : Événement onClick lié.")
        function()

