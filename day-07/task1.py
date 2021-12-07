puzzle_input = []

with open("day-07/input.txt") as f:
    puzzle_input = [int(num.strip()) for num in f.readlines()[0].split(",")]

print(f"Input: {puzzle_input}")

best = (None, None)

for pos in range(0, max(puzzle_input) + 1):
    cost = sum([abs(num - pos) for num in puzzle_input])
    print(f"{pos}: {cost}")
    if best[0] is None or cost < best[1]:
        best = (pos, cost)

print(best)