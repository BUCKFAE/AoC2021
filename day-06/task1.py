import sys

puzzle_input = []

with open("day-06/input.txt") as f:
    puzzle_input = [int(num.strip()) for num in f.readlines()[0].split(",")]

print(f"Input: {puzzle_input}")

DAYS = 256

new_population = []

for day in range(1, DAYS + 1):
    for fish in puzzle_input:
        new_fish_value = fish - 1 if fish > 0 else 6
        new_population.append(new_fish_value)
        if fish == 0:
            new_population.append(8)
    
    puzzle_input = [f for f in new_population]
    new_population.clear()
    print(f"Day {day}: {len(puzzle_input)}")

print(f"Fish after {DAYS} days: {len(puzzle_input)}")