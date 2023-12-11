from puzzleinput import lines
from copy import deepcopy

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
print(len(the_loop) // 2)
