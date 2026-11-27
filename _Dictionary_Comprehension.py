# Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]

# Create dictionary using comprehension
squares = {x: x * x for x in numbers}

print("Original Numbers:", numbers)
print("Squares Dictionary:", squares)

# Even numbers dictionary
even = {x: x for x in numbers if x % 2 == 0}

print("Even Numbers:", even)