a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
c=int(input("Enter the number c:"))

if a>b and a>c:
    print(a,"is greater than",b,"and",c)
elif b>a and b>c:
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",a,"and",b)