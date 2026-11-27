# Function to calculate simple interest
def simple_interest(p, r=5, t=2):
    si = (p * r * t) / 100
    print("Simple Interest:", si)

# Read principal amount
p = float(input("Enter principal amount: "))

# Function call
simple_interest(p)