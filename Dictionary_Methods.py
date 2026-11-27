# Create a dictionary
student = {
    "name": "Geethika",
    "age": 18,
    "marks": 90
}

# keys() method
print("Keys:", student.keys())

# values() method
print("Values:", student.values())

# items() method
print("Items:", student.items())

# get() method
print("Name:", student.get("name"))

# update() method
student.update({"marks": 95})
print("Updated:", student)

# pop() method
student.pop("age")
print("After pop:", student)

# copy() method
new_student = student.copy()
print("Copied Dictionary:", new_student)

# clear() method
student.clear()
print("After clear:", student)