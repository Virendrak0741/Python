#--------------------------------Exception Handling----------------------------#
#Example 1:
class InvalidAgeException(Exception):
    pass

number = 18  

try:
    input_number = int(input("Enter your age: "))
    if input_number < number:
        raise InvalidAgeException("Age is below 18")
    else:
        print("Eligible to vote.")
except InvalidAgeException as e:
    print("Not eligible to vote.", e)


#Eample 2:
try:
    n=0
    res=100/n
except ZeroDivisionError:
    print("You cannot divide a number by zero")

else:
    print("The result is",res)

finally:
    print("Execution completed")