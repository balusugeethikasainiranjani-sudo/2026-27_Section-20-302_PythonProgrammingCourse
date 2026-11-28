source = open("source.txt", "r")
content = source.read()
source.close()

destination = open("destination.txt", "w")
destination.write(content)
destination.close()

print("File content copied successfully")
