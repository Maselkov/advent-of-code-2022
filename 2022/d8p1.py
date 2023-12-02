from puzzleinput import lines

grid = [[int(tree) for tree in line] for line in lines]


def is_tree_visible(x1, y1):
    visible_left = True
    visible_right = True
    visible_up = True
    visible_down = True
    tree = grid[y1][x1]
    for x2 in range(len(grid[y])):
        if x2 == x1:
            continue
        if x2 < x1:
            if grid[y1][x2] >= tree:
                visible_left = False
        elif x2 > x1:
            if grid[y1][x2] >= tree:
                visible_right = False
    for y2 in range(len(grid)):
        if y2 == y1:
            continue
        if y2 < y1:
            if grid[y2][x1] >= tree:
                visible_up = False
        elif y2 > y1:
            if grid[y2][x1] >= tree:
                visible_down = False
    return visible_left or visible_right or visible_up or visible_down


visible = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if is_tree_visible(x, y):
            visible += 1
print(visible)
