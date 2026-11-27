# Create a nested dictionary

students = {
    "student1": {
        "name": "Geethika",
        "age": 18,
        "marks": 99
    },
    "student2": {
        "name": "Siri",
        "age": 19,
        "marks": 95
    }
}

# Access dictionary elements
print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Name:", students["student2"]["name"])

# Update marks
students["student1"]["marks"] = 95

# Display complete dictionary
print("Updated Dictionary:", students)