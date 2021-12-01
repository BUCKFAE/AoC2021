puzzle_input = []

with open("day-01/input.txt") as f:
    puzzle_input = [int(line.strip()) for line in f.readlines()]

print(puzzle_input)[:5]
res = sum([1 if puzzle_input[i] < puzzle_input[i+1] else 0 for i in range(len(puzzle_input) - 1)])
print(res)