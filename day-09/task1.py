puzzle_input = []

with open("day-09/input.txt") as f:
    puzzle_input = [[int(num) for num in row.strip()] for row in f.readlines()]

print("Puzzle input:\n{}\n\n".format("\n".join([str(num) for num in puzzle_input])))

risk_level = 0

for row_id, row in enumerate(puzzle_input):
    for col_id, col in enumerate(row):

        # Check left
        left_higher = True if col_id == 0 or row[col_id - 1] > col else False

        # Check right
        right_higher = True if col_id == len(row) - 1 or row[col_id + 1] > col else False

        # Check top
        top_higher = True if row_id == 0 or puzzle_input[row_id - 1][col_id] > col else False

        # Check bottom
        bottom_higher = True if row_id == len(puzzle_input) - 1 or puzzle_input[row_id + 1][col_id] > col else False

        # Determining risk level
        if left_higher and right_higher and top_higher and bottom_higher:
            risk_level += col + 1

            print("({}, {}):{} ({})".format(row_id, col_id, col, col))

print(risk_level)