# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Objects
a = Animal()
d = Dog()
c = Cat()

# Same method name, different outputs
a.speak()   # Animal makes a sound
d.speak()   # Dog barks
c.speak()   # Cat meows
