# COVID-19 State Case Tracker

## Overview
This Python program fetches COVID-19 data from the New York Times database and calculates the seven-day average of new cases for user-selected U.S. states. It compares the most recent week's average to the previous week's and reports the percentage change.

## Functionality
- Downloads COVID-19 data from the NYTimes GitHub repository.
- Tracks the 14 most recent days of new cases for each state.
- Allows users to input one or more states to analyze.
- Calculates and displays the seven-day average of new cases for the current and previous weeks, including the percentage increase or decrease.

## Usage
Run the program and enter state names when prompted:

python covid_tracker.py

## Code Breakdown
```python
def main():
    # Fetches and processes NYTimes data
    new_cases = calculate(reader)  # Builds 14-day case history
    # Handles state selection
    comparative_averages(new_cases, states)  # Prints averages

def calculate(reader):            # Constructs 14-day new cases dict
def comparative_averages(new_cases, states):  # Computes and displays averages