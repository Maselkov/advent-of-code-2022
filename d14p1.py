from puzzleinput import lines
from collections import defaultdict

cave = defaultdict(lambda: ".")

for line in lines:
    previous = None
    items = line.split(" -> ")
    for item in items:
        item = [int(coord) for coord in item.split(",")]
        if not previous:
            previous = item
            continue
        step = 1
        if previous[0] == item[0]:
            x = previous[0]
            if previous[1] > item[1]:
                step = -1
            for y in range(previous[1], item[1] + step, step):
                cave[(x, y)] = "#"
        elif previous[1] == item[1]:
            y = previous[1]
            if previous[0] > item[0]:
                step = -1
            for x in range(previous[0], item[0] + step, step):
                cave[(x, y)] = "#"
        previous = item


def print_cave(cave):
    min_x = min(x for x, y in cave)
    max_x = max(x for x, y in cave)
    min_y = min(y for x, y in cave)
    max_y = max(y for x, y in cave)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(cave[(x, y)], end="")
        print()


resting_sand = 0
max_y = max(y for x, y in cave)


def spawn_sand():
    x = 500
    y = 0
    while True:
        if y > max_y:
            return False
        elif cave[(x, y + 1)] == ".":
            y += 1
        elif cave[(x - 1, y + 1)] == ".":
            x -= 1
            y += 1
        elif cave[(x + 1, y + 1)] == ".":
            x += 1
            y += 1
        else:
            cave[(x, y)] = "o"
            return True


while True:
    spawned = spawn_sand()
    if not spawned:
        break
    resting_sand += 1
print_cave(cave)
print(resting_sand)
