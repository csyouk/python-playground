class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implrement abstract method")

class Cat(Animal):
    def talk(self):
        return "Meow"

class Dog(Animal):
    def talk(self):
        return "Bow wow"

class Cow(Animal):
    def behavior(self):
        return "eat"

animals = [Cat('Missy'),
           Cat('Mr. hello'),
           Dog('Lassie'),
           Cow('Poll')]



for animal in animals:
    print(animal.name + ":"+ animal.talk())
