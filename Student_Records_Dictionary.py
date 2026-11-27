# Create student records dictionary

students = {
    1: {"name": "Geethika", "marks": 90},
    2: {"name": "Siri", "marks": 85},
    3: {"name": "Ram", "marks": 95}
}

# Display student records
for roll_no, details in students.items():
    print("Roll Number:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print("----------------")

# Add a new student
students[4] = {"name": "Priya", "marks": 88}

# Display updated records
print("Updated Student Records:", students)