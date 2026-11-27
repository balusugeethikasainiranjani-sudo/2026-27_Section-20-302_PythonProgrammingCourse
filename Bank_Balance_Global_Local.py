# Global variable
balance = 5000

# Function to deposit money
def deposit(amount):
    global balance
    balance = balance + amount
    print("Deposited Amount:", amount)
    print("Current Balance:", balance)

# Function to withdraw money
def withdraw(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        print("Withdrawn Amount:", amount)
    else:
        print("Insufficient Balance")

# Function calls
deposit(2000)
withdraw(1000)

print("Final Bank Balance:", balance)