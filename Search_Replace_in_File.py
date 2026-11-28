file = open("sample.txt", "r")
content = file.read()
file.close()

search_word = input("Enter word to search: ")
replace_word = input("Enter word to replace: ")

new_content = content.replace(search_word, replace_word)

file = open("sample.txt", "w")
file.write(new_content)
file.close()

print("Word replaced successfully")
print("Updated File Content:")
print(new_content)