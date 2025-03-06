import csv
import requests
import sys


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state.capitalize() in new_cases:
            if state.capitalize() not in states:
                states.append(state)
        elif len(state) != 0:
            print("There is no state like this.")
        elif len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    for row in reader:
        state = row["state"]
        if state not in previous_cases:
            previous_cases[state] = 0

        cases_today = int(row["cases"])

        if state not in new_cases:
            new_cases[state] = []

        if len(new_cases[state]) == 0:
            new_cases[state].append(cases_today)
        else:
            new_cases[state].append(cases_today - previous_cases[state])

        if len(new_cases[state]) > 14:
            new_cases[state].pop(0)

        previous_cases[state] = cases_today

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    new_average = 0
    old_average = 0

    if len(states) == 0:
        print("There are no states to view")
        sys.exit()

    for row in new_cases:
        if row in states:
            for value in new_cases[row][:7]:
                old_average += int(value)

            for value in new_cases[row][7:]:
                new_average += int(value)

            old_average, new_average = old_average / 7, new_average / 7

            difference = new_average - old_average
            if difference >= 0:
                ind = "increase"
            else:
                ind = "decrease"

            try:
                percentage = int(abs((difference / old_average) * 100))
            except ZeroDivisionError:
                print("Error")
                sys.exit(1)

            print(
                f"{row} had a 7-day average of {int(new_average)} and a {ind} of {percentage}%"
            )


main()
