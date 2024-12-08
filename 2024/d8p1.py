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
    antinode_1 = (x1 - dx, y1 - dy)
    antinode_2 = (x2 + dx, y2 + dy)
    return antinode_1, antinode_2


antinode_positions = set()
for letter in antennas:
    for a, b in combinations(antennas[letter], 2):
        antinode_1, antinode_2 = get_antinodes(a, b)
        if 0 <= antinode_1[0] < x_max and 0 <= antinode_1[1] < y_max:
            antinode_positions.add(antinode_1)
        if 0 <= antinode_2[0] < x_max and 0 <= antinode_2[1] < y_max:
            antinode_positions.add(antinode_2)

print(len(antinode_positions))
