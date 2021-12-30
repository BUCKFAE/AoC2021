from typing import List, Dict
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

class Path:
    def __init__(self, path: List[str], lower_visited: Dict[str, int] = {}, lower_visited_twice: bool = False):
        self.path = path
        self.lower_visited = lower_visited
        self.lower_visited_twice = lower_visited_twice
    
    def can_extend_path(self, cave: str) -> bool:
        if cave == 'start':
            return False
        if cave == 'end':
            return True 

        # Big caves can be visited as often as we like
        if cave.isupper():
            return True

        # How often we visited this small cave
        visited = self.lower_visited.get(cave, 0)
        if visited > 0 and self.lower_visited_twice:
            return False
        
        return True

    def extend_path(self, cave: str):
        assert self.can_extend_path(cave)
        
        if cave.islower():
            self.lower_visited[cave] = self.lower_visited.get(cave, 0) + 1
            if self.lower_visited[cave] > 1:
                self.lower_visited_twice = True

        self.path.append(cave)

    def get_last_cave(self) -> str:
        return self.path[-1]

    def copy_path(self):
        return Path(self.path.copy(), lower_visited=self.lower_visited.copy(), lower_visited_twice=self.lower_visited_twice)

    def __repr__(self) -> str:
        return ' - '.join(self.path)

current_paths: List[Path] = [Path(['start'])]
finished_paths: List[Path] = []

while len(current_paths) > 0:

    new_paths: List[Path] = []

    for p in current_paths:


        # Getting the last cave of the path
        last_cave = p.get_last_cave()

        # All caves we can reach from the last cave
        possible_next_caves = paths[last_cave]

        # All possible continuations of that path
        for next_cave in possible_next_caves:

            if next_cave == 'end':
                path_copy = p.copy_path()
                path_copy.extend_path(next_cave)
                finished_paths.append(path_copy)

            elif p.can_extend_path(next_cave):
                path_copy = p.copy_path()
                path_copy.extend_path(next_cave)
                new_paths.append(path_copy)
                
    current_paths = [p.copy_path() for p in new_paths]
    new_paths.clear()

print('\n'.join([str(p) for p in finished_paths]))
print(len(finished_paths))