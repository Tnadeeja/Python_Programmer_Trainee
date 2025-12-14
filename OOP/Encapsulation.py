class Warrior:
    # Constructor (called when an object is created)
    def __init__(self, name):
        self.name = name      # public attribute
        self._age = 0         # protected attribute (encapsulation)

    # Getter method for age
    @property
    def age(self):
        return self._age

    # Setter method for age
    @age.setter
    def age(self, age):
        if age > 10:
            self._age = age
        else:
            print("Age should be greater than zero")

#creating instance
warrior1 = Warrior("worr1")

warrior1.age=5
print(warrior1.age)