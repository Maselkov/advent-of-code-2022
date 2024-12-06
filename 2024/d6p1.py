from puzzleinput import lines as lines

grid = []
positions = set()
for y, line in enumerate(lines):
    line = list(line)
    for x, char in enumerate(line):
        if char == "^":
            start = (x, y)
            line[x] = "."
    grid.append(line)


direction = (0, -1)
direction_order = [(0, -1), (1, 0), (0, 1), (-1, 0)]
x, y = start
positions.add((x, y))
while True:
    new_x = x + direction[0]
    new_y = y + direction[1]
    try:
        if new_x < 0 or new_y < 0:
            raise IndexError
        if grid[new_y][new_x] == "#":
            direction = direction_order[(direction_order.index(direction) + 1) % 4]
            continue
    except IndexError:
        break
    x = new_x
    y = new_y
    positions.add((x, y))
print(len(positions))
