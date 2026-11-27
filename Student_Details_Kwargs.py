# Function using **kwargs
def student_details(**details):
    print("Student Details:")

    for key, value in details.items():
        print(key, ":", value)

# Function call
student_details(
    name="Geethika",
    roll_no=101,
    course="B.Tech",
    branch="CSE",
    year=1
)
