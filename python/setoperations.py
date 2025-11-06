days1 = {"Monday", "Tuesday", "Wednesday","Thursday", "Friday"}
days2 = {"Thursday", "Friday", "Saturday"}
print("Unoin of Two sets:",days1|days2)

print("Intersection of two sets:",days1&days2)

print("Symmetric difference of sets:",days1 ^ days2)

print("Asymmetric difference of two sets:",days2 ^ days1)

print("is days1 is subset of days2?",days1.issubset(days2))

print("is days2 is subset of days1?",days2.issubset(days1))

print("is days1 is superset of days2?",days1.issuperset(days2))

print("is days2 is subset of days1?",days2.issubset(days1))

print("is days1 is disjoint of days2?",days1.isdisjoint(days2))

print("is days1 is equal of days2?",days1==days2)

print("is days1 is  not equal of days2?",days1!=days2)

print("conversion of set into list")
print("Days1 as a list",list(days1))
print("Days1 as a list",list(days2))