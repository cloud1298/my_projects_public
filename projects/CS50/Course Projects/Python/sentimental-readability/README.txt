# Readability Grade Calculator

## Overview
This Python program calculates the readability grade of a given text using the Coleman-Liau index. It analyzes the text's sentences, words, and letters to determine an approximate U.S. grade level required to understand it.

## Functionality
- Accepts text input from the user.
- Counts sentences, words, and letters.
- Applies the Coleman-Liau formula: `0.0588 * L - 0.296 * S - 15.8`
  - `L`: Average letters per 100 words
  - `S`: Average sentences per 100 words
- Outputs a grade level (e.g., "Grade 8", "Before Grade 1", "Grade 16+").

## Usage
Run the program and enter text when prompted:

python readability.py

## Code Breakdown
```python
def main():
    text = input("Text: ")          # Gets user text
    sentences = get_sentences(text) # Splits into sentences
    words = get_words(sentences)    # Extracts words
    # Calculates counts and grade
    print_grade(grade)              # Prints result

def get_sentences(text):           # Splits text into sentences
def get_words(sentences):          # Extracts alphabetic words
def calculate_sentences(sentences):# Counts sentences
def calculate_words(words):        # Counts words
def calculate_letters(words):      # Counts letters
def calculate_grade(...):          # Applies Coleman-Liau formula
def print_grade(grade):            # Formats and prints grade