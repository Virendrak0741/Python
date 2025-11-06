class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("marks:",self.marks)

s1=student("Virendra Katale",90)
s1.display()
