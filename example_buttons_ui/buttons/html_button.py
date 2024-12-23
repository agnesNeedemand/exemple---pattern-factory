from buttons.interfaces.button import Button

class HTMLButton(Button):
    def render(self):
        print("Render : Bouton au format HTML.")

    def on_click(self, function):
        print("HTMLButton : Événement onClick lié.")
        function()

