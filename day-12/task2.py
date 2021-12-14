from collections import Counter
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

sub = []

# TODO: This has to be a dynamic program, otherwise it will take forever
def extend_path(path):
    new_paths = []
    print(f"Extending path: {path}, cave: \"{path[-1]}\"")
    
    # Creating all possible paths
    for possible_cave in paths.get(path[-1], []):

        counts = Counter([c for c in path if c.islower()])

        # Visiting either big or unknown caves
        if possible_cave.isupper() or counts[possible_cave] == 0:
            new_paths.append(path + [possible_cave])
        
        if counts[possible_cave] < 2:
            if all([counts[c] < 2 for c in [c for c in path if c.islower() and c != possible_cave]]):
                new_paths.append(path + [possible_cave])
    

    if len(new_paths) == 0:
        return []

    # Recursively extending paths
    for new_path in new_paths:

        if sum([1 if cave == "end" else 0 for cave in new_path]) == 0 and sum([1 if cave == "start" else 0 for cave in new_path]) == 1:

            if ".".join(new_path) not in sub:
                
                sub.append(".".join(new_path))
                cave_paths.extend(extend_path(new_path))

    return new_paths


cave_paths += extend_path(["start"])

cave_paths = list(sorted(set([",".join(path) for path in cave_paths if len(path) > 0])))
print(cave_paths)
cave_paths = [p for p in cave_paths if p.endswith("end")]

print(cave_paths)
print(len(cave_paths))
for path in cave_paths:
    print(path)
print(len(cave_paths))