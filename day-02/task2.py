puzzle_input = []

with open("day-02/input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

x = 0
y = 0
aim = 0

for line in puzzle_input:
    direction, distance = line.split(" ")
    if direction == "forward":
        x += int(distance)
        y += aim * int(distance)
    elif direction == "down":
        aim += int(distance)
    elif direction == "up":
        aim -= int(distance)

print(f"{x=}, {y=}, {aim=}")
print(x * y)