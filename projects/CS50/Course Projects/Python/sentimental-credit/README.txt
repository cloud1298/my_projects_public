# Credit Card Validator

## Overview
This Python program validates credit card numbers using the Luhn algorithm and identifies the card type (AMEX, MASTERCARD, VISA) or declares it "INVALID". It takes a card number as input from the user and processes it to determine its validity and type.

## Functionality
- Accepts a card number as a numeric input (no spaces or hyphens).
- Applies the Luhn algorithm to validate the number.
- Identifies the card type based on length and starting digits:
  - AMEX: 15 digits, starts with 34 or 37
  - MASTERCARD: 16 digits, starts with 51-55
  - VISA: 13 or 16 digits, starts with 4
- Outputs the card type or "INVALID" if the number is invalid or unrecognized.

## Usage
Run the program and enter a card number when prompted:

python credit.py

## Code Breakdown
```python
def main():
    number = get_number()          # Gets card number as list of digits
    total_sum = calculate_total_sum(number)  # Applies Luhn algorithm
    print_card_type(total_sum, number)  # Determines and prints card type

def get_number():                  # Handles input validation
def calculate_total_sum(digits):   # Calculates Luhn sum
def print_card_type(total_sum, card_number):  # Identifies card type