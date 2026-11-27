# Global variable
count = 0

# Function to increment counter
def increment():
    global count
    count = count + 1
    print("Counter:", count)

# Function calls
increment()
increment()
increment()

print("Final Counter:", count)