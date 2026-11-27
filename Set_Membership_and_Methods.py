# Create a set
my_set = {10, 20, 30, 40, 50}

# Display the set
print("Original Set:", my_set)

# Membership operations
print("Is 20 present?", 20 in my_set)
print("Is 60 present?", 60 in my_set)

# Add an element
my_set.add(60)
print("After Add:", my_set)

# Update the set
my_set.update([70, 80])
print("After Update:", my_set)

# Remove an element
my_set.remove(30)
print("After Remove:", my_set)

# Discard an element
my_set.discard(100)
print("After Discard:", my_set)

# Find length
print("Length of Set:", len(my_set))