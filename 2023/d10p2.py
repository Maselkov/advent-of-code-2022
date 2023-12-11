from puzzleinput import lines
from copy import deepcopy
from matplotlib.path import Path


def is_point_in_polygon(polygon, point):
    p = Path(polygon)
    return p.contains_points([point])


to_replace = {"L": "┗", "J": "┛", "7": "┓", "F": "┏", "|": "┃", "-": "━", ".": " "}

diagram = []
starting_point = None
for y, line in enumerate(lines):
    line = list(line)
    if starting_point is None:
        try:
            starting_point = (line.index("S"), y)
        except ValueError:
            pass
    diagram.append(line)


def pretty_print(diagram):
    diagram_copy = deepcopy(diagram)
    for y, line in enumerate(diagram_copy):
        for x, char in enumerate(line):
            if char in to_replace:
                diagram_copy[y][x] = to_replace[char]
    for line in diagram_copy:
        print("".join(line))


the_loop = []
for xp, yp in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    if the_loop:
        break
    x, y = starting_point
    direction = (xp, yp)
    x += xp
    y += yp
    if diagram[y][x] is not None:
        direction = (xp, yp)
        points_visited = [(x, y)]
        while True:
            point = diagram[y][x]
            match diagram[y][x]:
                case "|":
                    if yp == 0:
                        break
                case "-":
                    if xp == 0:
                        break
                case "L":
                    if yp == 0:
                        if xp == 1:
                            break
                        xp = 0
                        yp = -1
                    else:
                        if yp == -1:
                            break
                        xp = 1
                        yp = 0
                case "J":
                    if yp == 0:
                        if xp == -1:
                            break
                        xp = 0
                        yp = -1
                    else:
                        if yp == -1:
                            break
                        xp = -1
                        yp = 0
                case "7":
                    if yp == 0:
                        if xp == -1:
                            break
                        xp = 0
                        yp = 1
                    else:
                        if yp == 1:
                            break
                        xp = -1
                        yp = 0
                case "F":
                    if yp == 0:
                        if xp == 1:
                            break
                        xp = 0
                        yp = 1
                    else:
                        if yp == 1:
                            break
                        xp = 1
                        yp = 0
                case "S":
                    the_loop = points_visited
                    break
            x += xp
            y += yp
            points_visited.append((x, y))
    else:
        continue
diff = (the_loop[-1][0] - the_loop[0][0], the_loop[-1][1] - the_loop[0][1])
if diff == (0, -1):
    diagram[starting_point[1]][starting_point[0]] = "F"

print(len(the_loop) // 2)
filtered_diagram = deepcopy(diagram)
for y, line in enumerate(filtered_diagram):
    for x, char in enumerate(line):
        if (x, y) not in the_loop:
            filtered_diagram[y][x] = "."

pretty_print(filtered_diagram)
path = Path(the_loop)
enclosed = 0
for y in range(len(diagram)):
    for x in range(len(diagram[y])):
        if (x, y) in the_loop:
            continue
        if path.contains_points([(x, y)]):
            enclosed += 1
print(enclosed)
