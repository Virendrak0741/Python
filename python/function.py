def input_data(n1 , n2):
    print("Number 1 : " , n1)
    print("Number 2 : " , n2)
print("Call the function..")
input_data(50, 30)

def input_data(n1 , n2 = 20):
    print("Number 1 : " , n1)
    print("Number 2 : " , n2)
print("Passing only one argument..")
input_data(50)

print("Passing two arguments..")
input_data(50, 30)

# Arbitary Arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Default Parameter value 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Returns value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Passing a list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Number of arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

