class Calculator:
    def add(self, *args):
        total = sum(args)
        print("Sum is:", total)

c = Calculator()

c.add(150, 50)
c.add(50, 100, 150)
c.add(10, 20, 30, 40, 50)