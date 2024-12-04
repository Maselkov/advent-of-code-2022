from puzzleinput import lines as grid

rows = len(grid)
cols = len(grid[0])
count = 0


def check_masness(x1, y1, x2, y2):
    if grid[x1][y1] == "M":
        if grid[x2][y2] == "S":
            return True
    else:
        if grid[x1][y1] == "S":
            if grid[x2][y2] == "M":
                return True
    return False


directions = [(-1, -1), (-1, 1)]
for x in range(1, rows - 1):
    for y in range(1, cols - 1):
        if grid[x][y] == "A":
            masful = True
            for direction in directions:
                dx, dy = direction
                if not check_masness(x + dx, y + dy, x - dx, y - dy):
                    masful = False
                    break
            if masful:
                count += 1
print(count)
