#constructor
class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
    
    def show(self):
        print("Brand Name : ",self.brand)
        print("Model Name : ",self.model)

c1 = Car("Toyota" , "Innova")
c1.show()

#Destructor
class Demo:
    def __init__(self):
        print("Constructor called")
    
    def __del__(self):
        print("Destructor called")

obj = Demo()
del obj