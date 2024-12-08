from puzzleinput import lines as lines
from collections import defaultdict
from itertools import combinations

antennas = defaultdict(list)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            antennas[char].append((x, y))

y_max = len(lines)
x_max = len(lines[0])


def get_antinodes(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    dx = x2 - x1
    dy = y2 - y1
    antinodes = [point_1, point_2]
    new_x = x1 - dx
    new_y = y1 - dy
    while 0 <= new_x < x_max and 0 <= new_y < y_max:
        antinodes.append((new_x, new_y))
        new_x -= dx
        new_y -= dy
    new_x = x2 + dx
    new_y = y2 + dy
    while 0 <= new_x < x_max and 0 <= new_y < y_max:
        antinodes.append((new_x, new_y))
        new_x += dx
        new_y += dy
    return antinodes


antinode_positions = set()
for letter in antennas:
    for a, b in combinations(antennas[letter], 2):
        antinodes = get_antinodes(a, b)
        for antinode in antinodes:
            antinode_positions.add(antinode)


print(len(antinode_positions))
