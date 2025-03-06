# DNA Sequence Matcher

## Overview
This Python program identifies a person by matching their DNA sequence against a database of individuals using Short Tandem Repeats (STRs). It reads a CSV database file and a DNA sequence text file, then determines if the sequence matches any person in the database.

## Functionality
- Loads a database of individuals with their STR counts from a CSV file.
- Reads a DNA sequence from a text file.
- Counts the longest consecutive repeats of each STR in the sequence.
- Matches the STR counts against the database to identify a person or returns "No match" if no match is found.

## Usage
Run the program with two command-line arguments:

python dna.py data.csv sequence.txt

- `data.csv`: CSV file containing the database of individuals and their STR counts.
- `sequence.txt`: Text file containing a single DNA sequence.

### Example
python dna.py database.csv dna1.txt

Output: Either a person's name (e.g., "Alice") or "No match".

## File Format
- **Database CSV**: First row contains column headers (e.g., `name,AGAT,AATG,TATC`), subsequent rows list individuals with their STR counts.
- **Sequence TXT**: Single line with a DNA sequence (e.g., `AGATAGATAGATAATG...`).

## Code Breakdown
```python
# Main function orchestrates the program flow
def main():
    check_argv()              # Validates command-line arguments
    database = get_database() # Loads CSV into list of dicts
    sequence = get_sequence() # Reads DNA sequence from file
    subsequences = get_subsequences(database, sequence) # Counts STR repeats
    find_person(database, subsequences) # Matches and prints result

# Key helper functions
def get_database()       # Loads CSV database
def get_sequence()       # Reads DNA sequence
def get_subsequences()   # Calculates STR counts
def longest_match()      # Finds longest consecutive STR repeats
def find_person()        # Matches sequence to database