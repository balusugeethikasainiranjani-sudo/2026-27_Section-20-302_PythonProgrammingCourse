# Function to calculate area and perimeter
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area of Rectangle:", area)
    print("Perimeter of Rectangle:", perimeter)

# Read input
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

# Function call
rectangle(length, breadth)