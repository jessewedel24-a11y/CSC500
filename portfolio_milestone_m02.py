"""
CSC500 - Principles of Programming
Module 2 Portfolio Milestone: Project Initialization and Variable Setup
Author: Jesse Wedel
Description: Foundation script for an online shopping cart application.
             Collects item names, descriptions, prices, and quantities from
             the user, then calculates subtotals and a cart total.
"""


def main():
    print("=== Online Shopping Cart ===\n")

    # --- Item 1 ---
    item1_name = input("Enter item 1 name: ")
    item1_description = input(f"Enter a description for {item1_name}: ")
    item1_price = float(input(f"Enter the price of {item1_name}: $"))
    item1_quantity = int(input(f"Enter the quantity of {item1_name}: "))

    # --- Item 2 ---
    item2_name = input("\nEnter item 2 name: ")
    item2_description = input(f"Enter a description for {item2_name}: ")
    item2_price = float(input(f"Enter the price of {item2_name}: $"))
    item2_quantity = int(input(f"Enter the quantity of {item2_name}: "))

    # --- Arithmetic: calculate subtotals per item ---
    item1_subtotal = item1_price * item1_quantity
    item2_subtotal = item2_price * item2_quantity

    # --- Arithmetic: calculate cart total ---
    cart_total = item1_subtotal + item2_subtotal

    # --- Display results ---
    print("\n=== Cart Summary ===")
    print(f"{item1_name} x{item1_quantity} @ ${item1_price:.2f} each = ${item1_subtotal:.2f}")
    print(f"  Description: {item1_description}")
    print(f"{item2_name} x{item2_quantity} @ ${item2_price:.2f} each = ${item2_subtotal:.2f}")
    print(f"  Description: {item2_description}")
    print(f"\nCart Total: ${cart_total:.2f}")


if __name__ == "__main__":
    main()
