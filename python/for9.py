n=int(input("Enter the number:"))
letter = ["A","B","C","D","E","F","G"]

for i in range(n):
    for j in range(i):
        print(letter[j],end=" ")
    print()