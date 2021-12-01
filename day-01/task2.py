puzzle_input = []

with open("day-01/input.txt") as f:
    puzzle_input = [int(line.split()[0].strip()) for line in f.readlines()]

print(puzzle_input)[:5]
res = sum([1 if (puzzle_input[i] + puzzle_input[i + 1] + puzzle_input[i + 2]) \
     < (puzzle_input[i + 1] + puzzle_input[i + 2] + puzzle_input[i + 3]) \
         else 0 for i in range(len(puzzle_input) - 3)])

print(res)