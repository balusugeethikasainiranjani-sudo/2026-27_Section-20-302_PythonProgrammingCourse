# Function to find GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Read input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Function call
result = gcd(a, b)

# Display output
print("GCD:", result)