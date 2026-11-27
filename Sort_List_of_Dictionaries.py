# Create a list of dictionaries

students = [
    {"name": "Geethika", "marks": 90},
    {"name": "Siri", "marks": 85},
    {"name": "Ram", "marks": 95}
]

# Sort students by marks
students.sort(key=lambda x: x["marks"])

# Display sorted list
print("Students Sorted by Marks:")

for student in students:
    print(student)