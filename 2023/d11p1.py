from puzzleinput import lines
import itertools

image = []
galaxies = {}
galaxy_id = 1
for line in lines:
    new_line = []
    for number in line:
        if number == "#":
            new_line.append(galaxy_id)
            galaxy_id += 1
        else:
            new_line.append(0)
    image.append(new_line)

expanded = []
for i, line in enumerate(image):
    expanded.append(line)
    if sum(line):
        continue
    expanded.append(line)
transposed = list(map(list, zip(*expanded)))
expanded_t = []
for i, line in enumerate(transposed):
    expanded_t.append(line)
    if sum(line):
        continue
    expanded_t.append(line)
transposed = list(map(list, zip(*expanded_t)))
expanded = transposed
for i, line in enumerate(expanded):
    for j, number in enumerate(line):
        if number:
            galaxies[number] = (i, j)


def pretty_print(image, emptiness=" "):
    for line in image:
        line = [str(x) for x in line]
        line = [x.replace("0", emptiness) for x in line]
        print("".join(line))


pretty_print(expanded, emptiness=".")


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


total = 0
print(len(list(itertools.combinations(galaxies.keys(), 2))))
for g1, g2 in itertools.combinations(galaxies.keys(), 2):
    distance = manhattan_distance(galaxies[g1], galaxies[g2])
    total += distance
print(total)
