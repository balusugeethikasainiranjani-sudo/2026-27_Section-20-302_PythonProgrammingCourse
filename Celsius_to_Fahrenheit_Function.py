# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Read input
celsius = float(input("Enter temperature in Celsius: "))

# Function call
result = celsius_to_fahrenheit(celsius)

# Display output
print("Temperature in Fahrenheit:", result)