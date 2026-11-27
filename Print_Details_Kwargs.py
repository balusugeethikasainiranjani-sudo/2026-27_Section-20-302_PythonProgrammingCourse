# Function using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Function call
print_details(name="Geethika", age=18, course="B.Tech", branch="CSE")