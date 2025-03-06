import csv

with open("helper.txt") as file:
    reader = csv.reader(file)

    for line in reader:
        for something in line:
            for letter in something:
                if letter == " ":
                    print("   ", end="")
                elif letter == '#':
                    print("H", end="")
                else:
                    print(letter, end="")
            print()