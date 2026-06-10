"""
calculator.py
CSC500 - Module 1 Critical Thinking Assignment
Basic arithmetic calculator: addition, subtraction, multiplication, division.
"""

import math


def get_number(prompt):
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            val = float(input(prompt))
            if not math.isfinite(val):
                raise ValueError
            return val
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def main():
    """Prompt for two numbers and display results for all four operations."""
    print("Basic Calculator")
    print("----------------")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    result_div = divide(num1, num2)

    print(f"\nResults:")
    print(f"  {num1} + {num2} = {num1 + num2}")
    print(f"  {num1} - {num2} = {num1 - num2}")
    print(f"  {num1} * {num2} = {num1 * num2}")

    if result_div is not None:
        print(f"  {num1} / {num2} = {result_div}")
    else:
        print(f"  {num1} / {num2} = undefined (cannot divide by zero)")


if __name__ == "__main__":
    main()
