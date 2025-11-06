employee = {
    'name': 'virendra',
    'age': 21,
    'department': 'IT',
     'skills': ['Python', 'Java', 'C++'],}
print(employee)

employee.update({"age":22})
print(employee)

print("Updated age:", employee['age'])


print(employee.pop("department"))
print("After popping department:", employee)

print(employee.popitem())
print("After popping last item:", employee)

print("Keys in Employee Dictionary:", employee.keys())
print("Values in Employee Dictionary:", employee.values())

print("Items in Employee Dictionary:", employee.items())
print("Checking if 'name' is in Employee Dictionary:", "name" in employee)

print(employee.setdefault("location", "India"))
print("After setdefault:", employee)


employee2=employee.copy()
print("Copied Employee Dictionary:", employee2)

employee2.clear()
print("Employee2 after clearing:", employee2)
