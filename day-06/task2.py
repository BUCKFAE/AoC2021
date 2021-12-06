import sys
from collections import Counter

puzzle_input = []

with open("day-06/input.txt") as f:
    puzzle_input = [int(num.strip()) for num in f.readlines()[0].split(",")]

print(f"Input: {puzzle_input}")

DAYS = 256

# Counts how ofte
new_population = Counter(puzzle_input)


for day in range(1, DAYS + 1):
    # Reduce the index for every count variable by one
    tmp = new_population.copy()
    for i in range(8):
        new_population[i] = tmp[i + 1] 

    new_population[8] = 0
    new_population[6] += tmp[0]
    new_population[8] += tmp[0]


print(f"Fish after {DAYS} days: {sum(new_population.values())}")