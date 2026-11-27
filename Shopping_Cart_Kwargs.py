# Function using **kwargs
def shopping_cart(**items):
    total = 0

    print("Shopping Cart:")

    for item, price in items.items():
        print(item, ":", price)
        total = total + price

    print("Total Amount:", total)

# Function call
shopping_cart(
    apple=50,
    banana=30,
    milk=40,
    bread=60
)