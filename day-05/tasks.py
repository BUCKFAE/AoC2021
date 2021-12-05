puzzle_input = []

with open("day-05/input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

# Finding the max coordinates
biggest_x_front = max([int(line.split(" -> ")[0].split(",")[0].strip()) for line in puzzle_input])
biggest_y_front = max([int(line.split(" -> ")[0].split(",")[1].strip()) for line in puzzle_input])
biggest_x_back = max([int(line.split(" -> ")[1].split(",")[0].strip()) for line in puzzle_input])
biggest_y_back = max([int(line.split(" -> ")[1].split(",")[1].strip()) for line in puzzle_input])
biggest_x = max(biggest_x_front, biggest_x_back)
biggest_y = max(biggest_y_front, biggest_y_back)

print(f"Board sizes: {biggest_x} x {biggest_y}")

board = [[0 for x in range(biggest_x + 1)] for y in range(biggest_y + 1)]
board_two = [[0 for x in range(biggest_x + 1)] for y in range(biggest_y + 1)]

for line in puzzle_input:

    start = [int(x) for x in line.split(" -> ")[0].strip().split(",")[::-1]]
    end = [int(x) for x in line.split(" -> ")[1].strip().split(",")[::-1]]

    # Horizontal line
    if start[0] == end[0]:

        line_start = min(start[1], end[1])
        line_end = max(start[1], end[1])

        for y in range(line_start, line_end + 1):
            board[start[0]][y] += 1
            board_two[start[0]][y] += 1
    
    # Vertical line
    elif start[1] == end[1]:
        line_start = min(start[0], end[0])
        line_end = max(start[0], end[0])
        for x in range(line_start, line_end + 1):
            board[x][start[1]] += 1
            board_two[x][start[1]] += 1
    
    # Diagonal line
    else:
        slope = (end[1] - start[1]) / (end[0] - start[0])
        b = start[1] - slope * start[0]
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            y = int(slope * x + b)
            board_two[x][y] += 1


# Amount of elements that are bigger than two
print(sum([sum(1 if field > 1 else 0 for field in row) for row in board]))
print(sum([sum(1 if field > 1 else 0 for field in row) for row in board_two]))
