puzzle_input = []

with open("day-03/input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

gamma_list = []
epsilon_list = []

for i in range(len(puzzle_input[0])):
    one = sum([1 if puzzle_input[j][i] == '1' else 0 for j in range(len(puzzle_input))])
    if one > len(puzzle_input) / 2:
        gamma_list.append('1')
        epsilon_list.append('0')
    else:
        gamma_list.append('0')
        epsilon_list.append('1')
    
gamma = int(''.join(gamma_list), 2)
epsilon = int(''.join(epsilon_list), 2)

print(gamma * epsilon)