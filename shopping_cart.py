class ItemToPurchase:
    """Represents a single item in an online shopping cart."""

    def __init__(self):
        """Default constructor -- initializes item with placeholder values."""
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        """Prints item name, quantity, price per unit, and total cost."""
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")


def main():
    cart = []

    print("Enter items for your cart. Type 'quit' as the item name to finish.\n")

    while True:
        item_name = input("Enter item name: ")

        if item_name.lower() == "quit":
            break

        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))

        item = ItemToPurchase()
        item.item_name = item_name
        item.item_price = item_price
        item.item_quantity = item_quantity

        cart.append(item)

    print("\nTOTAL COST")
    total_cost = 0.0

    for item in cart:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity

    print(f"Total: ${total_cost}")


if __name__ == "__main__":
    main()