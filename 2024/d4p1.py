from puzzleinput import lines as grid

word = "XMAS"
rows = len(grid)
cols = len(grid[0])
word_len = len(word)
count = 0


def check_direction(x, y, dx, dy):
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
            return False
    return True


directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
for x in range(rows):
    for y in range(cols):
        for dx, dy in directions:
            if check_direction(x, y, dx, dy):
                count += 1
print(count)
