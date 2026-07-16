"""
CSC500 - Principles of Programming
Module 6 Portfolio Milestone: Online Shopping Cart - Part 2
Author: Jesse Wedel

Description: Expands the shopping cart project with a ShoppingCart class
             that manages a collection of ItemToPurchase objects, plus a
             menu-driven interface for adding, removing, and modifying
             items, and viewing cart totals and descriptions.
"""


class ItemToPurchase:
    """Represents a single item available for purchase."""

    def __init__(self):
        """Default constructor -- initializes item with placeholder values."""
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        """Prints item name, quantity, price per unit, and total cost."""
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    def print_item_description(self):
        """Prints item name and description."""
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """Manages a customer's collection of ItemToPurchase objects."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """Initializes cart with customer info and an empty item list."""
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Adds an ItemToPurchase object to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Removes an item by name. Prints a message if not found."""
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        """Updates an existing item's attributes using a temp ItemToPurchase.

        Only non-default fields on the passed-in item are applied, so a
        caller can update just the quantity (for example) without
        clobbering the existing price or description.
        """
        for existing_item in self.cart_items:
            if existing_item.item_name == item.item_name:
                if item.item_description != "none":
                    existing_item.item_description = item.item_description
                if item.item_price != 0.0:
                    existing_item.item_price = item.item_price
                if item.item_quantity != 0:
                    existing_item.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """Returns the total quantity of all items in the cart."""
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """Returns the total cost of all items in the cart."""
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        """Displays the full cart with totals, or an empty-cart message."""
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        """Displays the description of every item in the cart."""
        print(f"{self.customer_name}'s Shopping Cart - Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    """Runs the interactive menu loop for the given ShoppingCart."""
    menu_text = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    while True:
        print(menu_text)
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            item = ItemToPurchase()
            item.item_name = input("Enter the item name: ")
            item.item_description = input("Enter the item description: ")
            item.item_price = float(input("Enter the item price: "))
            item.item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(item)

        elif choice == "r":
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == "c":
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            temp_item = ItemToPurchase()
            temp_item.item_name = item_name
            temp_item.item_quantity = new_quantity
            cart.modify_item(temp_item)

        elif choice == "i":
            cart.print_descriptions()

        elif choice == "o":
            cart.print_total()

        elif choice == "q":
            print("Exiting the menu.")
            break

        else:
            print("Invalid option. Please try again.")


def main():
    """Collects customer info, builds a ShoppingCart, and starts the menu."""
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
