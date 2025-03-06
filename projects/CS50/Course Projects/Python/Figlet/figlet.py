import sys
import random
from pyfiglet import Figlet


def main():
    figlet = preparation()

    text = input("Input: ")
    print(figlet.renderText(text))


def preparation():
    figlet = Figlet()
    list = figlet.getFonts()

    if len(sys.argv) not in [1, 3] or (len(sys.argv) == 3 and (sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in list)):
        print('Program usage: "python ProgramName.py" or "python ProgramName.py -f FontName" or "python program.py --font FontName"')
        sys.exit(1)

    if len(sys.argv) == 1:
        number = random.randrange(0, len(list))
        figlet.setFont(font=list[number])
    else:
        figlet.setFont(font=sys.argv[2])

    return figlet


if __name__ == '__main__':
    main()