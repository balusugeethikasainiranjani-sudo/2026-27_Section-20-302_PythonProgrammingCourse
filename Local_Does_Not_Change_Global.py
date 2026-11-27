# Global variable
x = 10

def display():
    # Local variable
    x = 20
    print("Local x:", x)

# Function call
display()

print("Global x:", x)
