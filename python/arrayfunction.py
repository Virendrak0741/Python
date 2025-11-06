import array as arr

numbers = arr.array('i', [10, 20, 30, 40, 50])
print(numbers)

print("Created Array:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)  # insert 25 at index 2
print("After insert:", numbers)

# removes element at index 3
print("After pop:", numbers)

numbers.remove(20)  # removes first 20
print("After remove:", numbers)

numbers.reverse()
print("After reverse:", numbers)x

extra = arr.array('i', [70, 80, 90])
numbers.extend(extra)
print("After extend:", numbers)

print("Count of 30:", numbers.count(30))

print("Buffer Info:", numbers.buffer_info())

print("Typecode of array:", numbers.typecode)

