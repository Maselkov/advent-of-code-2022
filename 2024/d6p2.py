from puzzleinput import lines as lines
from copy import deepcopy

data = []
for y, line in enumerate(lines):
    line = list(line)
    for x, char in enumerate(line):
        if char == "^":
            start = (x, y)
            line[x] = "."
    data.append(line)


def simulate_guard(grid):
    positions = set()
    direction = (0, -1)
    direction_order = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y = start
    positions.add((x, y, direction))
    while True:
        new_x = x + direction[0]
        new_y = y + direction[1]
        pos = (new_x, new_y, direction)
        if pos in positions:
            return True
        try:
            if new_x < 0 or new_y < 0:
                raise IndexError
            if grid[new_y][new_x] == "#":
                direction = direction_order[(direction_order.index(direction) + 1) % 4]
                continue
        except IndexError:
            return False
        x = new_x
        y = new_y
        positions.add((x, y, direction))


total_number_of_positions = len(data) * len(data[0])
total = 0
i = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        i += 0
        if data[y][x] == "#":
            continue
        new_data = deepcopy(data)
        new_data[y][x] = "#"
        if simulate_guard(new_data):
            total += 1
print(total)
