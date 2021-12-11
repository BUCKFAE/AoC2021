puzzle_input = []

with open("day-11/input.txt") as f:
    puzzle_input = [[int(n) for n in row.strip()] for row in f.readlines()]

def print_grid(grid):
    print("\n".join(["".join([str(n) for n in row]) for row in grid]))

print_grid(puzzle_input)

total_flashes_count = 0

for current_step in range(1, 10001):
    print(f"Step: {current_step}")

    to_increase = [(y, x) for x in range(len(puzzle_input)) for y in range(len(puzzle_input))]

    flashes = []

    flashes_this_step = 0
    for y, x in to_increase:
        puzzle_input[y][x] += 1
        if puzzle_input[y][x] > 9:
            flashes_this_step += 1
            flashes.append((y, x))

    while flashes:
        y, x = flashes.pop()

        # Horizontal
        if x > 0:
            puzzle_input[y][x - 1] += 1
            if puzzle_input[y][x - 1] == 10:
                flashes_this_step += 1
                flashes.append((y, x - 1))
        if x < len(puzzle_input) - 1:
            puzzle_input[y][x + 1] += 1
            if puzzle_input[y][x + 1] == 10:
                flashes_this_step += 1
                flashes.append((y, x + 1))

        # Vertical
        if y > 0:
            puzzle_input[y - 1][x] += 1
            if puzzle_input[y - 1][x] == 10:
                flashes_this_step += 1
                flashes.append((y - 1, x))
        if y < len(puzzle_input) - 1:
            puzzle_input[y + 1][x] += 1
            if puzzle_input[y + 1][x] == 10:
                flashes_this_step += 1
                flashes.append((y + 1, x))

        # Diagonal
        if x > 0 and y > 0:
            puzzle_input[y - 1][x - 1] += 1
            if puzzle_input[y - 1][x - 1] == 10:
                flashes_this_step += 1
                flashes.append((y - 1, x - 1))
        if x < len(puzzle_input) - 1 and y < len(puzzle_input) - 1:
            puzzle_input[y + 1][x + 1] += 1
            if puzzle_input[y + 1][x + 1] == 10:
                flashes_this_step += 1
                flashes.append((y + 1, x + 1))
        if x > 0 and y < len(puzzle_input) - 1:
            puzzle_input[y + 1][x - 1] += 1
            if puzzle_input[y + 1][x - 1] == 10:
                flashes_this_step += 1
                flashes.append((y + 1, x - 1))
        if x < len(puzzle_input) - 1 and y > 0:
            puzzle_input[y - 1][x + 1] += 1
            if puzzle_input[y - 1][x + 1] == 10:
                flashes_this_step += 1
                flashes.append((y - 1, x + 1))
            

    total_flashes_count += flashes_this_step

    # Checking if all octopuses flashed this round
    if flashes_this_step == len(puzzle_input) * len(puzzle_input):
        print(f"All octopuses flashed in step {current_step}")
        break

    for x in range(len(puzzle_input)):
        for y in range(len(puzzle_input)):
            if puzzle_input[y][x] > 9:
                puzzle_input[y][x] = 0        

    print_grid(puzzle_input)

print(total_flashes_count)
