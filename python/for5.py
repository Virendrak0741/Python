num=int(input("Enter the number:"))
sum=0
fact=1

for i in range(1, num+1):
    fact*=i
    sum+=1/fact
sum+=1          #to add first term
print("Sum is:",sum)