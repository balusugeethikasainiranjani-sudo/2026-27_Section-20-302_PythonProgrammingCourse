# Function using *args
def find_sum(*args):
    total = 0

    for i in args:
        total = total + i

    print("Sum:", total)

# Function call
find_sum(10, 20, 30, 40, 50)