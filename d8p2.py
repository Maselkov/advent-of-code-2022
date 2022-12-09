from puzzleinput import lines

grid = [[int(tree) for tree in line] for line in lines]


def calculate_scenic_score(x1, y1):
    scenic_score = 1
    tree = grid[y1][x1]
    viewing_distance = 0
    options = [
        (x1 - 1, -1, -1),
        (x1 + 1, len(grid[y1])),
        (y1 - 1, -1, -1),
        (y1 + 1, len(grid)),
    ]
    for c, option in enumerate(options):
        viewing_distance = 0
        for i in range(*option):
            if c in (0, 1):
                x2 = i
                y2 = y1
            else:
                x2 = x1
                y2 = i
            if x2 == x1 and y2 == y1:
                continue
            if grid[y2][x2] >= tree:
                viewing_distance += 1
                break
            else:
                viewing_distance += 1
        scenic_score *= viewing_distance
        viewing_distance = 0
    return scenic_score


highest = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        score = calculate_scenic_score(x, y)
        if score > highest:
            highest = score
print(highest)
