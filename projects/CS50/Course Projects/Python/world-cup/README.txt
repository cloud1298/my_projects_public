# Sports Tournament Simulator

## Overview
This Python program simulates a single-elimination sports tournament based on team ratings. It reads team data from a CSV file, runs 1000 tournament simulations, and calculates each team's probability of winning.

## Functionality
- Loads team names and ratings from a CSV file.
- Simulates games using a logistic probability model based on rating differences.
- Conducts multiple rounds until one team remains.
- Runs 1000 tournaments and reports each team's win percentage.

## Usage
Run the program with a CSV file as an argument:

python tournament.py teams.csv

## File Format
- **CSV**: Must have columns `team` (name) and `rating` (integer).
  Example:

team,rating
Team A,1500
Team B,1400
Team C,1300
Team D,1200

## Code Breakdown
```python
N = 1000  # Number of simulations

def main():
  teams = []  # Loads teams from CSV
  counts = {} # Tracks wins
  # Runs N simulations
  # Prints win probabilities

def simulate_game(team1, team2):    # Simulates one game
def simulate_round(teams):          # Simulates one round
def simulate_tournament(teams):     # Runs full tournament