import sys


def main():
    # Get value of dollars from the user and calculate how many coins are needed
    dollars = get_dollars()
    calculate_coins(dollars)


def get_dollars():
    """
    Ask the user for input and handle errors.

    Returns:
        float:  The entered dollar amount.
    """
    while True:
        try:
            dollars = float(input("Change owed: "))
            if dollars == round(dollars, 2) and dollars > 0:
                return dollars
            print("Enter currency value.")
        except ValueError:
            print("Please enter the number.")
        except EOFError:
            print()
            sys.exit()


def calculate_coins(dollars):
    """
    Calculate the number of coins needed for the given dollar amount and print the result.

    Args:
        dollars (float): The dollar amount for which coins need to be calculated.
    """
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    num_coins = 0

    # Calculate the number of each type of coin with value bigger than 0.01
    coin_types = [quarter, dime, nickel]
    for coin_value in coin_types:
        if dollars >= coin_value:
            num_coins += int(dollars / coin_value)
            dollars = round((dollars % coin_value), 2)

    # Calculate the number of pennies
    if dollars > 0:
        num_coins += int(dollars * 100)

    # Print the result
    print(f"{num_coins} coins.")


if __name__ == "__main__":
    main()
