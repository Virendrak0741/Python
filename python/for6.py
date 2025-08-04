import math

x=float(input("Enter x in radian:"))
n=int(input("Enter the number of terms:"))

cos=0
sign=1

for i in range(n):
    power=2*i
    term=(x**power)/math.factorial(power)
    cos+=sign*term          #add or subtract the term
    sign+=-1

print("cos(x)=",cos)