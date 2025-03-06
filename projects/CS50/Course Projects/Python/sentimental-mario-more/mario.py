import sys


def main():
    # Get the pyramid height from the user and print the pyramid
    height = get_height()
    print_pyramid(height)


def get_height():
    # Get user input for pyramid height(between 1 and 8) and handle errors
    while True:
        try:
            height = int(input("Height (1-8): "))
            if 1 <= height <= 8:
                return height
            print("Only numbers between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")
        except EOFError:
            print()
            sys.exit()


def print_pyramid(height):
    # Print a pyramid with two spaces between each row
    for row in range(1, height + 1):
        # Calculate the number of white spaces before the "#" characters
        wh_spaces = height - row

        # Print the white spaces
        print(" " * wh_spaces, end="")

        # Print the first set of "#" characters
        print("#" * row, end="  ")

        # Print the second set of "#" characters
        print("#" * row)


if __name__ == "__main__":
    main()
