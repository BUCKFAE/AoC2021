import re
import sys
import numpy as np

puzzle_input = []

# Loading puzzle input
with open("day-04/input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

numbers = [int(n) for n in puzzle_input[0].split(",")]
print(f"Numbers that will be drawn: {numbers}")

board_strings = "\n".join(puzzle_input[1:]).split("\n\n")

# Creating 2D int list with all numbers on the board
boards = []
marks = []

# Creating boards and marks
for board in board_strings:
    boards.append(np.array([int(n) for n in board.replace("\n", " ").split(" ") if n.strip()], dtype=int).reshape(5, 5))
    marks.append(np.zeros(shape=(5, 5), dtype=bool))

# Playing until we found a winner
for number in numbers:
    print(f"Current number: {number}")

    for board in range(len(boards)):

        # Marking matches
        for match in np.column_stack(np.where(boards[board] == number)):
            marks[board][match[0]][match[1]] = True

        # Checking for victory
        row_win = [np.all(marks[board][i] == True) for i in range(5)]
        col_win = [np.all(np.transpose(marks[board])[i] == True) for i in range(5)]

        # A board won
        if any(row_win) or any(col_win):
            res = 0
            for row in range(5):
                for col in range(5):
                    if not marks[board][row][col]:
                        res += boards[board][row][col]

            print(f"Result: {res * number}")
            
            sys.exit()
                        

