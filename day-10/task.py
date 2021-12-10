puzzle_input = []

with open("day-10/input.txt") as f:
    puzzle_input = [row.strip() for row in f.readlines()]


points = {")": 3, "]": 57, "}": 1197, ">": 25137}

total_score = 0

corrupted_indices = []

line_scores = []

for idx, line in enumerate(puzzle_input):
    print(f"\nCurrent line: \"{line}\"")

    stack = []

    brackets = {")": 0, "]": 0, "}": 0, ">": 0}
    for char in line:

        invalid = False

        if char == "(":
            stack.append(char)
        elif char == ")":
            res = stack.pop()
            if res != "(":
                invalid = True
        elif char == "[":
            stack.append(char)
        elif char == "]":
            res = stack.pop()
            if res != "[":
                invalid = True
        elif char == "{":
            stack.append(char)
        elif char == "}":
            res = stack.pop()
            if res != "{":
                invalid = True
        elif char == "<":
            stack.append(char)
        elif char == ">":
            res = stack.pop()
            if res != "<":
                invalid = True

        if invalid:
            print(f"\nFound a bad line: \"{line}\"")
            total_score += points[char]
            corrupted_indices.append(idx)
            break
    
    # Task 2
    if idx not in corrupted_indices:
        completion_scores = {")": 1, "]": 2, "}": 3, ">": 4}
        line_score = 0
        for remaining_char in stack[::-1]:
            if remaining_char == "(":
                line_score = (line_score * 5) + completion_scores[")"]
            elif remaining_char == "[":
                line_score = (line_score * 5) + completion_scores["]"]
            elif remaining_char == "{":
                line_score = (line_score * 5) + completion_scores["}"]
            elif remaining_char == "<":
                line_score = (line_score * 5) + completion_scores[">"]

        line_scores.append(line_score)


print(f"Task1: Total score: {total_score}")

res2 = sorted(line_scores)[int(len(line_scores) / 2)]
print(f"Task2: Total score: {res2}")

