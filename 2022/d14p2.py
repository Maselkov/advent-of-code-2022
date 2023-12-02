from puzzleinput import lines
from collections import defaultdict


class Cave(defaultdict):
    def __init__(self):
        super().__init__(lambda: ".")
        self.max_y = float("inf")

    def __getitem__(self, __key):
        if __key[1] == self.max_y:
            return "#"
        return super().__getitem__(__key)


cave = Cave()


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
floor = max_y + 2
cave.max_y = floor


def spawn_sand():
    x = 500
    y = 0
    while True:
        if cave[(x, y + 1)] == ".":
            y += 1
        elif cave[(x - 1, y + 1)] == ".":
            x -= 1
            y += 1
        elif cave[(x + 1, y + 1)] == ".":
            x += 1
            y += 1
        else:
            cave[(x, y)] = "o"
            if x == 500 and y == 0:
                print("squished")
                return False
            return True


while True:
    spawned = spawn_sand()
    resting_sand += 1
    if not spawned:
        break
print(resting_sand)
