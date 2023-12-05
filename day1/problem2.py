# Advent of Code 2023 - Day 1
# Problem 2

import os

data = {}
with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
        data[count] = line
    

def find_numbers(line: str) -> list:
    """
    Find all occurrences of number words or digits in a line and return their positions.

    :param line: The line of text to search.
    :return: A list of tuples, each containing the number word or digit and its position in the line.
    """
    
    targets = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    positions = []
    for target in targets:
        pos = line.find(target)
        while pos != -1:
            positions.append((target, pos))
            pos = line.find(target, pos + 1)
    return sorted(positions, key=lambda x: x[1])  # Sort by position

def match_int(text: str or int) -> int:
    # Check if input is already an integer
    if isinstance(text, int):
        return text

    # Mapping of text to integers
    text_to_int = {
        'one': 1, '1': 1,
        'two': 2, '2': 2,
        'three': 3, '3': 3,
        'four': 4, '4': 4,
        'five': 5, '5': 5,
        'six': 6, '6': 6,
        'seven': 7, '7': 7,
        'eight': 8, '8': 8,
        'nine': 9, '9': 9
    }

    # Return the corresponding integer, or None if not found
    return text_to_int.get(text)

def collect_numbers(data: dict) -> list:
    # this function goes through each line in the input data dictionary
    # and finds all candidates for numbers in the string
    # then it sorts the candidates by position in the string
    # and converts the first and last candidates to integers
    # Then it appends them to a list
    # which which it returns
    numbers = []
    for _, line in data.items():
        candidates = find_numbers(line)
        if candidates:
            low = match_int(candidates[0][0])  # First element's number
            high = match_int(candidates[-1][0])  # Last element's number
            numbers.append(low * 10 + high)
    return numbers


to_sum = collect_numbers(data)
answer = sum(to_sum)
print(f"answer is {answer}")

