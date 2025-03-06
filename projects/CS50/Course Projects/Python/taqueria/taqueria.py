list = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    print_items()
    calculate_price()


def print_items():
    print("Select item from the list: ", end="\n\n")
    for item in list:
        print(item)
    print()

def calculate_price():
    price = 0

    try:
        while True:
            item = input("Item: ")
            item = item.title()
            if item in list:
                price += list[item]
                print(f"Total: ${price:.2f}")
    except EOFError:
        print()
        exit()


if __name__ == "__main__":
    main()