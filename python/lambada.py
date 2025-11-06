#maping
nums=[1,2,3,4]
squares=list(map(lambda x:x**2,nums))
print(squares)

#with filter
nums=[1,2,3,4,5]
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

#with reduce
from functools import reduce
product=reduce(lambda x,y:x*y,[1,2,3,4])
print(product)

