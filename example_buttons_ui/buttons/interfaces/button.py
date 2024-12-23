from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        """Méthode pour le rendu du bouton."""
        pass

    @abstractmethod
    def on_click(self, function):
        """Méthode pour lier un événement click."""
        pass

