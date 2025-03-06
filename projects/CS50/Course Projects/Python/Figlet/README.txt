# Text Banner Generator

## Overview
This Python program generates ASCII art banners from user input using the `pyfiglet` library. It supports random font selection or specific font selection via command-line arguments.

## Functionality
- Prompts the user for text input.
- Converts the input into an ASCII art banner using a font from the `pyfiglet` library.
- Supports two modes:
  - No arguments: Uses a randomly selected font.
  - With arguments: Uses a specified font.

## Usage
Run the program with one of these commands:

python banner.py

python banner.py -f fontname

python banner.py --font fontname

- `-f` or `--font`: Specifies the font (e.g., `slant`, `standard`).
- `fontname`: Must be a valid font from the `pyfiglet` library.

### Example
python banner.py -f slant

## Code Breakdown
```python
def main():
    figlet = preparation()      # Sets up the Figlet object with font
    text = input("Input: ")     # Gets user input
    print(figlet.renderText(text))  # Prints ASCII art

def preparation():
    figlet = Figlet()           # Initializes Figlet
    list = figlet.getFonts()    # Gets available fonts
    # Validates command-line arguments
    # Sets random font if no args, specified font otherwise
    return figlet