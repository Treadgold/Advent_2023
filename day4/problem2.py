def calculate_score(line: str) -> int:
    """Calculates the score based on the intersection of winner and guess sets."""
    winners, guesses = (set(map(int, part.split())) for part in line.split(":")[1].split("|"))
    return len(winners.intersection(guesses))

def process_lines(file_path: str) -> int:
    """Processes each line of the file and calculates the total based on scores."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    multiplicity = [1] * len(lines)

    for index, line in enumerate(lines):
        win_count = calculate_score(line)
        for i in range(1, win_count + 1):
            if index + i < len(multiplicity):
                multiplicity[index + i] += multiplicity[index]

    return sum(multiplicity)


file_name = "input.txt"
total_score = process_lines(file_name)
print(f"total={total_score}")
