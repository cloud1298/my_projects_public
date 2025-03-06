import csv
import sys
import os


def main():
    # Check if number of arguments is correct
    check_argv()

    # Load database into the variable (list of dicts. 1 dict - 1 person)
    database = get_database()

    # Load DNA sequence into the variable (one string)
    sequence = get_sequence()

    # Get all subsequences (one dict)
    subsequences = get_subsequences(database, sequence)

    # Find matched person and print it's name or "No match" if not found
    find_person(database, subsequences)


def check_argv():
    """
    Check number of arguments and exit when the number is invalid.
    """
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)


def get_database():
    """
    Load database from file as the list of dictionaries and handle error when file is not found.

    Returns:
        List of dictionaries with person name and number of each subsequence repeats.
    """
    database = []
    # Get the name of file from the command line argument
    filename_database = sys.argv[1]

    try:
        with open(filename_database) as file:
            # Load file into reader
            reader = csv.DictReader(file)

            # Append every person into the list
            for line in reader:
                database.append(line)

        return database

    except FileNotFoundError:
        # Print error with base file name excluding path
        print(f'There is no file named "{os.path.basename(filename_database)}".')
        sys.exit(2)


def get_sequence():
    """
    Load person DNA sequence from the file and handle error when file is not found.

    Returns:
        Single DNA sequence string.
    """
    # Get file name from the command line argument
    filename_sequence = sys.argv[2]

    try:
        with open(filename_sequence) as file:
            # Read the DNA sequence and get rid of and white chars
            sequence = file.readline().strip()

        return sequence

    except FileNotFoundError:
        # Print error with base file name excluding path
        print(f'There is no file named "{os.path.basename(filename_sequence)}".')
        sys.exit(2)


def get_subsequences(database, sequence):
    """
    Get the dictionary of subsequences as a key and biggest repeat count as a value.

    Args:
        database: List of dictionaries with each person name and subsequences biggest repeat count.
        sequence: Single DNA sequence string

    Returns:
    Dictionary with each substring as a key, and the biggest number of repeats as a value

    """
    # make a set of subsequences based on the database (excluding "name" key)
    subsequences = set(key for key in database[0] if key != "name")
    subsequence_count = {}

    for item in subsequences:
        # Get the longest subsequence repeat
        longest = longest_match(sequence, item)

        # Load subsequence and count into the dictionary
        subsequence_count[item] = longest

    return subsequence_count


def longest_match(sequence, subsequence):
    """
    Returns length of longest run of subsequence in sequence.

    Args:
        sequence: Single string of DNA sequence
        subsequence: Single string of DNA subsequence

    Returns:
        Number containing length of longest run of subsequence in sequence.
    """

    # Initialize variables
    i = 0
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    while i < sequence_length:
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches

        while sequence[i : i + subsequence_length] == subsequence:
            count += 1
            i += subsequence_length

            # Update most consecutive matches found
        if count > 0:
            longest_run = max(longest_run, count)
        i += 1

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def find_person(database, subsequences):
    # Check database for matching profiles
    for person in database:
        found = True
        for subsequence, value in subsequences.items():
            if person[subsequence] and person[subsequence] != str(value):
                found = False
                break
        if found:
            print(person["name"])
            sys.exit()

    print("No match")
    sys.exit()


if __name__ == "__main__":
    main()
