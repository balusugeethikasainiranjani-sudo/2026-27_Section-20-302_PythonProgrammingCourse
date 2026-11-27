
text = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for i in text:
    if i == ch:
        count = count + 1

print("Character frequency:", count)
