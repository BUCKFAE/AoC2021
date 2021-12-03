puzzle_input = []

with open("day-03/input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

remaining_gamma = [n for n in puzzle_input]
remaining_epsilon = [n for n in puzzle_input]

for i in range(len(puzzle_input[0])):
    one_g = sum([1 if remaining_gamma[j][i] == '1' else 0 for j in range(len(remaining_gamma))])
    one_e = sum([1 if remaining_epsilon[j][i] == '1' else 0 for j in range(len(remaining_epsilon))])

    if len(remaining_gamma) > 1:

        if one_g >= len(remaining_gamma) / 2:
            remaining_gamma = [g for g in remaining_gamma if g[i] == '1']
        else:
            remaining_gamma = [g for g in remaining_gamma if g[i] == '0']

    if len(remaining_epsilon) > 1:
        if one_e < len(remaining_epsilon) / 2:
            remaining_epsilon = [e for e in remaining_epsilon if e[i] == '1']
        else:
            remaining_epsilon = [e for e in remaining_epsilon if e[i] == '0']

gamma = int(remaining_gamma[0], 2)
epsilon = int(remaining_epsilon[0], 2)


print(gamma * epsilon)