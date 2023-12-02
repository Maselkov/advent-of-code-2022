import math
from puzzleinput import lines

visited_points = set()
ordered_points = []
hx = 0
hy = 0
knots = [[0, 0] for _ in range(10)]
for line in lines:
    line = line.split()
    direction, distance = line[0], int(line[1])
    for _ in range(distance):
        match direction:
            case "R":
                hx += 1
            case "L":
                hx -= 1
            case "U":
                hy += 1
            case "D":
                hy -= 1
        for i, knot in enumerate(knots):
            if i == 0:
                px = hx
                py = hy
            else:
                px = knots[i - 1][0]
                py = knots[i - 1][1]

            kx = knot[0]
            ky = knot[1]
            diffx = px - kx
            diffy = py - ky
            if abs(diffx) + abs(diffy) == 1:
                if i == 8:
                    visited_points.add((kx, ky))
                    ordered_points.append((kx, ky))
                continue
            if px != kx and py != ky:
                if abs(diffx) + abs(diffy) <= 2:
                    if i == 8:
                        visited_points.add((kx, ky))
                        ordered_points.append((kx, ky))
                    continue
                kx += int(math.copysign(1, diffx) * 1)
                ky += int(math.copysign(1, diffy) * 1)
            elif px == kx and py != ky:
                ky += diffy // 2
            elif py == ky and px != kx:
                kx += diffx // 2
            if i == 8:
                visited_points.add((kx, ky))
                ordered_points.append((kx, ky))
            knot[0] = kx
            knot[1] = ky
            knots[i] = knot

print(len(visited_points))
