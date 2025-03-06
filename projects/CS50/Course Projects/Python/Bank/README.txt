# Greeting Cost Evaluator

## Overview
This is a simple Python program that evaluates a user-provided greeting and assigns a cost based on specific rules. The program takes a greeting as input, processes it, and outputs a dollar amount.

## Functionality
The program determines the cost of a greeting according to these rules:
- If the first word of the greeting is "hello" (case-insensitive), the cost is `$0`.
- If the first word starts with "h" (case-insensitive) but isn't "hello", the cost is `$20`.
- For all other greetings, the cost is `$100`.

## Usage
1. Run the program in a Python environment.
2. Enter a greeting when prompted (e.g., "Hello there", "Hi friend", "Good morning").
3. The program will output the cost as `$0`, `$20`, or `$100`.

### Example Inputs and Outputs
| Input            | Output |
|------------------|--------|
| `Hello world`    | `$0`   |
| `Hi there`       | `$20`  |
| `Good day`       | `$100` |

## Code Breakdown
```python
greeting = input("Greeting: ")       # Prompts user for input
words = greeting.split()             # Splits input into a list of words
if "hello" in words[0].lower():      # Checks if first word is "hello"
    print("$0")
elif words[0][0].lower() == "h":     # Checks if first word starts with "h"
    print("$20")
else:                                # All other cases
    print("$100")