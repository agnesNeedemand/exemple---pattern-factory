import random

class User:

    def __init__(self):
        self.id = None
        self.lastname = None
        self.firstname = None

    

class UserFactory:

    _id = 1
    _lastname = ["Dupont", 'Durand', "Lopez", "Martin"]
    _firstname = ["John", "Jeanne", "Manon", "Marc"]

    @classmethod
    def create_fake_user(cls):
        user = User()
        # id
        user.id= cls._id
        cls._id = cls._id + 1 # auto-incrementation

        # Randomly select lastname and firstname
        user.lastname = random.choice(cls._lastname)
        user.firstname = random.choice(cls._firstname)

        return user


# Exemple d'utilisation
factory = UserFactory()

for i in range(10):
    fake_user = factory.create_fake_user()
    print(f"ID: {fake_user.id}, Prénom: {fake_user.firstname}, Nom: {fake_user.lastname}")