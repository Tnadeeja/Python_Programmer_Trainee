from abc import ABC, abstractmethod

# Abstract class
class Warrior(ABC):

    def __init__(self, name):
        self.name = name

    # Abstract method (no implementation)
    @abstractmethod
    def attack(self):
        pass

# Child class 1
class Swordsman(Warrior):

    def attack(self):
        return f"{self.name} attacks with a sword!"

# Child class 2
class Archer(Warrior):

    def attack(self):
        return f"{self.name} attacks with a bow!"

w1 = Swordsman("Arthur")
w2 = Archer("Robin")

print(w1.attack())
print(w2.attack())
