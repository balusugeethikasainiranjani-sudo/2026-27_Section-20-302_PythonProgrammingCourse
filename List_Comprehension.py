# Create a dictionary
student = {
    "name": "Geethika",
    "age": 18,
    "marks": 90
}

# Iterate using for loop
print("Dictionary Elements:")

for key in student:
    print(key, ":", student[key])

# Iterate using items()
print("Using items() method:")

for key, value in student.items():
    print(key, ":", value)