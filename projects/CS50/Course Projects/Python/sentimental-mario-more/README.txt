# Pyramid Printer

## Overview
This Python program creates a double-sided pyramid of hashtags (`#`) based on a user-specified height. The pyramid has two identical halves separated by two spaces, resembling the classic Mario-style pyramid.

## Functionality
- Prompts the user for a pyramid height between 1 and 8.
- Prints a pyramid with:
  - Left-aligned spaces decreasing as rows increase.
  - Two sets of `#` characters per row, separated by two spaces.
  - Row count matching the specified height.

## Usage
Run the program and enter a height when prompted:

python pyramid.py

## Code Breakdown
```python
def main():
    height = get_height()     # Gets valid height from user
    print_pyramid(height)     # Prints the pyramid

def get_height():             # Handles input validation
    # Loops until valid integer 1-8 is entered
    # Returns height

def print_pyramid(height):    # Constructs and prints pyramid
    # Loops through rows, printing spaces and hashtags