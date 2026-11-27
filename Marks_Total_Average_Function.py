# Function to calculate total and average
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    print("Total Marks:", total)
    print("Average Marks:", average)

# Read marks
m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))

# Function call
calculate_marks(m1, m2, m3)