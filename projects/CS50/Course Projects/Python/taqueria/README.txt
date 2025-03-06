# Taqueria Order Calculator

## Overview
This Python program simulates a taqueria ordering system. It displays a menu of items with prices, allows the user to input items to order, and calculates the running total cost.

## Functionality
- Displays a predefined menu of taqueria items and their prices.
- Accepts user input for items to order.
- Adds the price of each valid item to a running total.
- Shows the updated total after each item is added.

## Usage
Run the program and enter items from the menu:

python taqueria.py

Press Ctrl+D or Ctrl+Z to exit.

## Code Breakdown
```python
list = {...}  # Dictionary of menu items and prices

def main():
    print_items()       # Displays menu
    calculate_price()   # Handles ordering and total calculation

def print_items():      # Prints menu items
def calculate_price():  # Calculates and displays running total