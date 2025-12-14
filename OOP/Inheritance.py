# Parent class
class Warrior:
    def __init__(self, name):
        self.name = name      # Public attribute
        self._age = 0         # Protected attribute (encapsulation)

    # Getter method to access age
    @property
    def age(self):
        return self._age

    # Setter method to update age safely
    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age should be greater than zero")

    # Common method for all warriors
    def attack(self):
        print(self.name, "is attacking!")

# Child class inherits from Warrior
class Knight(Warrior):
    def __init__(self, name, weapon):
        super().__init__(name)   # Call parent constructor
        self.weapon = weapon    # New attribute for Knight

    def defend(self):
        print(self.name, "is defending with", self.weapon)

# Another child class inherits from Warrior
class Archer(Warrior):
    def __init__(self, name, arrows):
        super().__init__(name)   # Call parent constructor
        self.arrows = arrows    # New attribute for Archer

    def shoot(self):
        print(self.name, "is shooting arrows. Arrows left:", self.arrows)

# Create Knight object
k1 = Knight("Arthur", "Sword")
k1.age = 25          # Using encapsulation (setter)
k1.attack()          # Inherited method
k1.defend()          # Knight's own method
print(k1.age)        # Getter method

# Create Archer object
a1 = Archer("Robin", 10)
a1.age = 20          # Using encapsulation
a1.attack()          # Inherited method
a1.shoot()           # Archer's own method
