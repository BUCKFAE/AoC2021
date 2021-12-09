puzzle_input = []

with open("day-09/input.txt") as f:
    puzzle_input = [[int(num) for num in row.strip()] for row in f.readlines()]

print("Puzzle input:\n{}\n\n".format("\n".join([str(num) for num in puzzle_input])))

def get_adjacent_tiles(x, y):
        adjacent_tiles = []
        if x > 0:
            adjacent_tiles.append(puzzle_input[x - 1][y])
        if x < len(puzzle_input) - 1:
            adjacent_tiles.append(puzzle_input[x + 1][y])
        if y > 0:
            adjacent_tiles.append(puzzle_input[x][y - 1])
        if y < len(puzzle_input[0]) - 1:
            adjacent_tiles.append(puzzle_input[x][y + 1])
        return adjacent_tiles

def get_adjacent_coordinates(x, y):
        adjacent_tiles = []
        if x > 0:
            adjacent_tiles.append((x - 1, y))
        if x < len(puzzle_input) - 1:
            adjacent_tiles.append((x + 1, y))
        if y > 0:
            adjacent_tiles.append((x, y - 1))
        if y < len(puzzle_input[0]) - 1:
            adjacent_tiles.append((x, y + 1))
        return adjacent_tiles

def extend_basin(x, y, basin):
    
    adjacent = get_adjacent_coordinates(x, y)
    for coord in adjacent:
        if puzzle_input[coord[0]][coord[1]] != 9 and coord not in basin:
            basin.append(coord)
            extend_basin(coord[0], coord[1], basin)
    return basin

risk_level = 0

basins = []

for row_id, row in enumerate(puzzle_input):
    for col_id, col in enumerate(row):

        if all([t > col for t in get_adjacent_tiles(row_id, col_id)]):
            risk_level += col + 1

            print("({}, {}):{} ({})".format(row_id, col_id, col, col))
            basin = extend_basin(row_id, col_id, [(row_id, col_id)])
            basins.append(basin)

biggest_three = sorted(basins, key=lambda basin: len(basin))[-3:]
res = len(biggest_three[0]) * len(biggest_three[1]) * len(biggest_three[2])
print(res)