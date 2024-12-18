from dialogs.dialog import Dialog
from dialogs.web_dialog import WebDialog
from dialogs.windows_dialog import WindowsDialog


class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self, os_type):
        """Initialisation selon le type d'OS."""
        if os_type == "Windows":
            self.dialog = WindowsDialog()
        elif os_type == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Erreur ! Système d'exploitation inconnu.")

    def main(self, os_type):
        self.initialize(os_type)
        self.dialog.render()

if __name__ == "__main__":
    # Simulation de configuration
    os_type = "Windows"  # Remplacer "Windows" par "Web" pour changer de plateforme.
    app = Application()
    app.main(os_type)

    print()

    os_type = "Web"
    app.main(os_type)

