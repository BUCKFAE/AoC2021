puzzle_input = []

with open("day-12/input.txt") as f:
    puzzle_input = [row.strip() for row in f.readlines()]

print("\n".join(puzzle_input))

big_caves = []
small_caves = []
paths = {}

for line in puzzle_input:
    start, end = line.split("-")

    # Starting point
    if start.islower() and start not in small_caves:
        small_caves.append(start)
    elif start.isupper() and start not in big_caves:
        big_caves.append(start)

    # End point
    if end.islower() and end not in small_caves:
        small_caves.append(end)
    elif end.isupper() and end not in big_caves:
        big_caves.append(end)

    # Path
    if start not in paths:
        paths[start] = []
    if end not in paths:
        paths[end] = []
    paths[start].append(end)
    paths[end].append(start)

print("Small caves: {}".format(small_caves))
print("Big caves: {}".format(big_caves))
print("Paths: {}".format(paths))

cave_paths = []

def extend_path(path):
    new_paths = []
    print(f"Extending path: {path}, cave: \"{path[-1]}\"")
    
    # Creating all possible paths
    for possible_cave in paths.get(path[-1], []):
        print(f"Possible path: {possible_cave}")

        # Visiting either big or unknown caves
        if possible_cave.isupper() or possible_cave not in path:
            new_paths.append(path + [possible_cave])
    
    print(f"New paths: {new_paths}")

    if len(new_paths) == 0:
        return []

    # Recursively extending paths
    for new_path in new_paths:
        
        cave_paths.extend(extend_path(new_path))

    return new_paths


cave_paths += extend_path(["start"])

cave_paths = [path for path in cave_paths if len(path) > 0]
print(cave_paths)
cave_paths = [p for p in cave_paths if p[-1] == "end"]

print(cave_paths)
print(len(cave_paths))
for path in cave_paths:
    print(",".join(path))
print(len(cave_paths))