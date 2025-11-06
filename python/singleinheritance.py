#Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows.")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.sound()
cat.sound()