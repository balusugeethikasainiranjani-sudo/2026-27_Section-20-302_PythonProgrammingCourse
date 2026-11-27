# Read two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap using tuple unpacking
a, b = b, a

# Display swapped values
print("After swapping:")
print("First number:", a)
print("Second number:", b)