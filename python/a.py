#number=[1, 2, 3, 4, 5]
#number.sort(reverse=True)
#print(number)

#no=[1,2,4,5,7,5,3]
#s=sorted(no)
#print(s)
#print(no)

#list comprehension
#(shorter way to create a list)
'''li=[]
for i in range(1,6):
    li.append(i*i)
print(li)

#list comprehension
li=[i*i for i in range(1,6)]
print(li)

squ=[i**2 for i in range(1,6)]
print(squ)

even=[i for i in range(1,11) if i%2==0]
print(even)

odd=[i for i in range(1,11) if i%2!=0]
print(odd)

fruits=['apple','banana','cherry']
upper_fruits=[fruit.upper() for fruit in fruits]
print(upper_fruits)

text="123abc456def"
numbers=[int(char) for char in text if char.isdigit()]
print(numbers)

text="campus credemtial"
vowels=[i for i in text if i in 'a'or'e'or'i'or'o'or'u']
print(vowels)

even=[i for i in range(1,10) if i%2==0]
print(even)

sentence="lern python programming"
text=sentence.split()
print(text)

rev=[text[::-1] for text in sentence.split()]
print(rev)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
list1=[j for i in matrix for j in i]    
print(list1)  

squared=[j**2 for i in matrix for j in i]
print(squared)

li=[1,"hello",2,3,10,5,'hi']
str_list=[i for i in li if isinstance(i,str)]
print(str_list)

data=[i for i in li if type(i)==int]
print(data)

text=["apple","banana","cherry"]
data1=len(text[1])
print(data1)
length=[len(i) for i in text]
print(length)

text=["madam","hello","racecar","level"]
palindrome=[i for i in text if i==i[::-1]]
print(palindrome)'''

#dictionary comprehension(mtable)
dict1={
    "name": "Virendra",
    "city": "Kolhapur"

}
print(dict1["name"])
print(dict1["city"])

dict={
    "a":"1"
}
dict.clear()
print(dict)

#copying the dictionary
dict2=dict1.copy()
print(dict2)

#fromkeys
keys=["a","b","c"]
dict3=dict1.fromkeys(keys,0)
print(dict3)

#get
print(dict1.get("name"))
print(dict1.get("age", 25)) 


