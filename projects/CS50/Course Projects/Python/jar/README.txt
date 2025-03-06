# Cookie Jar Simulator

## Overview
This Python program implements a `Jar` class to simulate a cookie jar with a fixed capacity. It allows depositing and withdrawing cookies, tracks the current number of cookies, and displays the jar's contents using cookie emojis.

## Functionality
- Creates a jar with a default capacity of 12 cookies (customizable).
- Supports adding cookies (`deposit`) and removing cookies (`withdraw`).
- Displays the jar's contents as a string of cookie emojis (`🍪`) or "Empty jar" if empty.
- Provides read-only access to the jar's capacity and current size via properties.

## Usage
Run the program directly to see a basic example:

python jar.py

### Example Usage in Python
```python
jar = Jar(10)      # Create a jar with capacity 10
jar.deposit(5)     # Add 5 cookies
print(jar)         # Output: There are 🍪🍪🍪🍪🍪 cookies in the jar!
jar.withdraw(2)    # Remove 2 cookies
print(jar)         # Output: There are 🍪🍪🍪 cookies in the jar!

class Jar:
    def __init__(self, capacity=12)  # Initializes jar with capacity
    def __str__(self)                # Returns string representation with emojis
    def deposit(self, n)             # Adds n cookies, checks capacity
    def withdraw(self, n)            # Removes n cookies, checks availability
    @property def capacity(self)     # Returns jar capacity
    @property def size(self)         # Returns current number of cookies

def main():
    jar = Jar()         # Creates default jar
    jar.deposit(5)      # Adds 5 cookies
    jar.withdraw(1)     # Removes 1 cookie
    print(str(jar))     # Prints jar state