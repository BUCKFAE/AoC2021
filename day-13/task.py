import numpy as np

puzzle_input = []

with open("day-13/input.txt") as f:
    file_content = f.readlines()
    puzzle_board = [tuple([int(i) for i in row.strip().split(',')]) for row in file_content if row.strip() and not row.startswith('fold')]
    folding_instructions = [row.strip().removeprefix('fold along').strip() for row in file_content if row.strip() and row.startswith('fold')]

print('\n'.join([f'({t[0]}, {t[1]})' for t in puzzle_board]))
print('\n'.join(folding_instructions))

# Bounds are the biggest x and y values in the puzzle board plus 1 as coordinates start at (0, 0)
size_x = max([x[0] for x in puzzle_board]) + 1
size_y = max([x[1] for x in puzzle_board]) + 1

paper = np.zeros((size_y, size_x), dtype=bool)

# Marking Paper
for x, y in puzzle_board:
    paper[y, x] = True

def print_paper(paper: np.ndarray):
    print('Paper:\n' + '\n'.join([''.join(['#' if x else '.' for x in row]) for row in paper]))

def fold_paper(paper: np.ndarray, instruction: str):

    # Folding along y axis:
    if 'y' in instruction:
        fold_coordinate = int(instruction.split('=')[1])

        upper_part = paper[:fold_coordinate, :]
        lower_part = paper[fold_coordinate + 1:, :][::-1]

        folded = np.logical_or(upper_part, lower_part)
    elif 'x' in instruction:
        fold_coordinate = int(instruction.split('=')[1])

        left_part = paper[:, :fold_coordinate]
        right_part = np.flip(paper[:, fold_coordinate + 1:], axis=1)

        # Padding right vector with zeroes so it has the same shape
        pad_vector = np.zeros((left_part.shape[0], left_part.shape[1] - right_part.shape[1]))
        right_part = np.append(pad_vector, right_part, axis=1)

        folded = np.logical_or(left_part, right_part)
    else:
        raise ValueError
    return folded

# print_paper(paper)
print(f'{folding_instructions=}')

for fold_instruction in folding_instructions:
    paper = fold_paper(paper, fold_instruction)


print_paper(paper)

# Counts how often True in paper
print(f'{paper.sum()}')