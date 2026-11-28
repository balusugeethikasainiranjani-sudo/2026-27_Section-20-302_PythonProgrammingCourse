class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter vehicle speed: "))

    if speed < 0:
        raise InvalidSpeedError("Speed cannot be negative")

    print("Vehicle speed:", speed)

except InvalidSpeedError as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid number")