from puzzleinput import lines
import itertools

increase_factor = 10000

image = []
galaxies = {}
galaxy_id = 1
for y, line in enumerate(lines):
    new_line = []
    for x, number in enumerate(line):
        if number == "#":
            new_line.append(galaxy_id)
            galaxies[galaxy_id] = (x, y)
            galaxy_id += 1
        else:
            new_line.append(0)
    image.append(new_line)

y = 0
for line in image:
    if sum(line):
        y += 1
        continue
    # Increase galaxies with Y higher than this by 10
    for galaxy in galaxies:
        if galaxies[galaxy][1] > y:
            galaxies[galaxy] = (
                galaxies[galaxy][0],
                galaxies[galaxy][1] + increase_factor - 1,
            )
    y += increase_factor

transposed = list(map(list, zip(*image)))
x = 0
for line in transposed:
    if sum(line):
        x += 1
        continue
    # Increase galaxies with X higher than this by 10
    for galaxy in galaxies:
        if galaxies[galaxy][0] > x:
            galaxies[galaxy] = (
                galaxies[galaxy][0] + increase_factor - 1,
                galaxies[galaxy][1],
            )
    x += increase_factor


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


total = 0
print(len(list(itertools.combinations(galaxies.keys(), 2))))
for g1, g2 in itertools.combinations(galaxies.keys(), 2):
    distance = manhattan_distance(galaxies[g1], galaxies[g2])
    total += distance
print(total)
