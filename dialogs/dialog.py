from abc import ABC, abstractmethod
from buttons.interfaces.button import Button

class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        """Méthode factory pour créer un bouton."""
        pass

    def render(self):
        """Appelle create_button pour obtenir un produit \
            et l'utiliser."""
        ok_button: Button = self.create_button()
        ok_button.on_click(self.close_dialog)
        ok_button.render()

    def close_dialog(self):
        print("Fermeture du dialogue.")

