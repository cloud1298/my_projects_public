# Coin Change Calculator

## Overview
This Python program calculates the minimum number of coins needed to make change for a given dollar amount. It uses US coin denominations (quarters, dimes, nickels, and pennies) and accepts a user-provided dollar amount.

## Functionality
- Prompts the user for a positive dollar amount.
- Calculates the fewest coins needed using:
  - Quarters ($0.25)
  - Dimes ($0.10)
  - Nickels ($0.05)
  - Pennies ($0.01)
- Outputs the total number of coins required.

## Usage
Run the program and enter a dollar amount when prompted:

python change.py

## Code Breakdown
```python
def main():
    dollars = get_dollars()      # Gets valid dollar amount from user
    calculate_coins(dollars)     # Calculates and prints coin count

def get_dollars():               # Handles input validation
    # Loops until valid positive float is entered
    # Returns dollar amount

def calculate_coins(dollars):    # Computes minimum coins needed
    # Uses greedy algorithm with coin denominations
    # Prints total number of coins