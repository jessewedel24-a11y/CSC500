"""
Restaurant Meal Calculator
CSC500 - Module 3 Critical Thinking Assignment
"""


def calculate_meal_totals(food_charge):
    """Calculate tip, tax, and total for a restaurant meal."""
    tip = food_charge * 0.18
    tax = food_charge * 0.07
    total = food_charge + tip + tax
    return tip, tax, total


def main():
    """Prompt user for food charge and display meal cost breakdown."""
    food_charge = float(input("Enter the food charge: $"))

    tip, tax, total = calculate_meal_totals(food_charge)

    print(f"\nTip (18%):  ${tip:.2f}")
    print(f"Tax (7%):   ${tax:.2f}")
    print(f"Total:      ${total:.2f}")


if __name__ == "__main__":
    main()