## --------- Hierarchical Inheritance -----------

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "works as an employee")

class Manager(Person):  
    def role(self):
        print(self.name, "is a Manager")

e = Employee("Virendra Katale")
e.role()

m = Manager("Virendra Katale")
m.role()