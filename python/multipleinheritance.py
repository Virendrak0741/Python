class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def display(self):
        print(f"Name:",self.name)
        print(f"Salary:", self.salary)

e1=Employee("Virendra", 50000)
e1.display()
