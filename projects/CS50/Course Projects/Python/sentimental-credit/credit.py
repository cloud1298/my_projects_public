import sys


def main():
    # Get the number from the user
    number = get_number()

    # Calculate the sum of card number digits
    total_sum = calculate_total_sum(number)

    # Print the card type or "INVALID" if the card is not recognized
    print_card_type(total_sum, number)


def get_number():
    """
    Get the card number from the user, convert it into a list of digits, and handle errors.

    Returns:
        List of digits extracted from the card number
    """
    while True:
        try:
            card_number = int(input("Number (without spaces and hyphens): "))
            digits = [int(digit) for digit in str(card_number)]
            return digits
        except ValueError:
            print("Only the numbers")
        except EOFError:
            print()
            sys.exit()


def calculate_total_sum(digits):
    """
    Calculate the total sum of card number digits.

    Args:
        digits: List of digits from the card number

    Returns:
        Calculated total sum of digits
    """
    first_nums = sum(digits[-1::-2])  # Sum of overy first digit from the right

    second_nums = sum(
        digit * 2 if digit * 2 < 10 else 1 + (2 * digit) % 10
        for digit in digits[-2::-2]
    )  # Sum of every other doubled digits with adjustment

    return first_nums + second_nums


def print_card_type(total_sum, card_number):
    """
    Determine the card type based on the total sum and print the result.

    Args:
        total_sum: Total sum of card number digits
        card_number: List of digits from the card number

    """
    if total_sum % 10 == 0:
        first_digits = card_number[:2]

        if len(card_number) == 15 and (
            first_digits == [3, 4] or first_digits == [3, 7]
        ):
            print("AMEX")
        elif len(card_number) == 16 and (
            first_digits[0] == 5 and first_digits[1] in [1, 2, 3, 4, 5]
        ):
            print("MASTERCARD")
        elif len(card_number) in [13, 16] and first_digits[0] == 4:
            print("VISA")
        else:
            raise ValueError("INVALID")
    else:
        raise ValueError("INVALID")


if __name__ == "__main__":
    try:
        main()

    # If there is a ValueError, print "INVALID"
    except ValueError as e:
        print(e)
