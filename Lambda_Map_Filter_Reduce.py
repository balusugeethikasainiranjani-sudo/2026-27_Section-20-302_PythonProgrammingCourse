from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Lambda function
square = lambda x: x * x
print("Square:", square(5))

# Map function
result = list(map(lambda x: x * 2, numbers))
print("Map:", result)

# Filter function
result = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter:", result)

# Reduce function
result = reduce(lambda x, y: x + y, numbers)
print("Reduce:", result)