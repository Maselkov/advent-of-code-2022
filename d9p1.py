from puzzleinput import lines
import math

visited_points = set()
ordered_points = []
hx = 0
hy = 0
tx = 0
ty = 0
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
        diffx = hx - tx
        diffy = hy - ty
        if abs(diffx) + abs(diffy) == 1:
            visited_points.add((tx, ty))
            ordered_points.append((tx, ty))
            continue
        if hx != tx and hy != ty:
            if abs(diffx) + abs(diffy) <= 2:
                visited_points.add((tx, ty))
                ordered_points.append((tx, ty))
                continue
            tx += int(math.copysign(1, diffx) * 1)
            ty += int(math.copysign(1, diffy) * 1)
        elif hx == tx and hy != ty:
            ty += diffy // 2
        elif hy == ty and hx != tx:
            tx += diffx // 2
        visited_points.add((tx, ty))
        ordered_points.append((tx, ty))
print(len(visited_points))
