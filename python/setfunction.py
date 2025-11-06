days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
print(days)
print(type(days))

days.add("Sunday")
print(days)

days.remove("Monday")
print(days)

days.pop()
print(days)

days_copy=days.copy()
print("Copied Set",days_copy)

days.discard("Friday")
print("set after discarding friday",days)