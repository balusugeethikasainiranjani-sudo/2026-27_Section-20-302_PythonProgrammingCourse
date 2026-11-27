# Function to find factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Read input
num = int(input("Enter a number: "))

# Function call
result = factorial(num)

# Display output
print("Factorial:", result)