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

def match_int(text: str) -> int:
    # all this does is convert the text to an integer
    if text == 'one' or text == '1':
        return 1
    elif text == 'two' or text == '2':
        return 2
    elif text == 'three' or text == '3':
        return 3
    elif text == 'four' or text == '4':
        return 4
    elif text == 'five' or text == '5':
        return 5
    elif text == 'six' or text == '6':
        return 6
    elif text == 'seven' or text == '7':
        return 7
    elif text == 'eight' or text == '8':
        return 8
    elif text == 'nine' or text == '9':
        return 9
    else:
        return None

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

