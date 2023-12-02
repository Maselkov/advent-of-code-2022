from puzzleinput import lines

maze = []

for y, line in enumerate(lines):
    row = []
    for x, character in enumerate(line):
        if character == "S":
            start = (x, y)
            character = "a"
        elif character == "E":
            end = (x, y)
            character = "z"
        row.append(ord(character) - ord("a"))
    maze.append(row)


def find_shortest_path(maze, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) == end:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(maze[0])
                and 0 <= ny < len(maze)
                and maze[ny][nx] <= maze[y][x] + 1
            ):
                queue.append(((nx, ny), steps + 1))


print(find_shortest_path(maze, start, end))
