"""
CSC500 - Module 5 Critical Thinking Assignment
Option 1: Average Rainfall (Nested Loops)

Collects monthly rainfall data across a user-specified number of years
and displays the total months tracked, total rainfall, and average
rainfall per month.
"""


def get_positive_int(prompt):
    """Prompt the user until a positive whole number is entered.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: A validated positive integer.
    """
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value <= 0:
            print("Please enter a number greater than zero.")
            continue
        return value


def get_rainfall(prompt):
    """Prompt the user until a valid non-negative rainfall amount is entered.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: A validated non-negative rainfall amount in inches.
    """
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")
            continue
        if value < 0:
            print("Rainfall cannot be negative.")
            continue
        return value


def main():
    """Collect rainfall data across multiple years and display the average."""
    num_years = get_positive_int("Enter the number of years: ")

    total_months = 0
    total_rainfall = 0.0

    # Outer loop: one iteration per year
    for year in range(1, num_years + 1):
        # Inner loop: one iteration per month (12 months per year)
        for month in range(1, 13):
            prompt = f"Year {year}, month {month} rainfall (inches): "
            monthly_rainfall = get_rainfall(prompt)
            total_rainfall += monthly_rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months

    print(f"\nTotal months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")


if __name__ == '__main__':
    main()
