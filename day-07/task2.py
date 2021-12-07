puzzle_input = []

with open("day-07/input.txt") as f:
    puzzle_input = [int(num.strip()) for num in f.readlines()[0].split(",")]

print(f"Input: {puzzle_input}")

best = (None, None)

for pos in range(0, max(puzzle_input) + 1):
    cost = 0
    for crab in puzzle_input:
        new_crab_pos = crab
        steps = 1
        while new_crab_pos != pos:
            if new_crab_pos > pos:
                new_crab_pos -= 1
            else:
                new_crab_pos += 1

            cost += steps
            steps += 1

    print(f"{pos}: {cost}")
    if best[0] is None or cost < best[1]:
        best = (pos, cost)

print(best)