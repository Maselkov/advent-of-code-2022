from puzzleinput import lines

grid = []
for line in lines:
    grid_line = []
    for character in line:
        if character == ".":
            grid_line.append(None)
        else:
            grid_line.append(character)
    grid.append(grid_line)

total = 0
numbers = []
gears = []
for x in range(0, len(grid)):
    current_number = []
    start_pos = None
    for y in range(0, len(grid[x])):
        char = grid[x][y]
        if char is not None and char.isdigit():
            current_number.append(char)
            if start_pos is None:
                start_pos = (x, y)
        elif start_pos is not None:
            number = int("".join(current_number))
            current_number = []
            numbers.append((number, start_pos))
            start_pos = None
        if char is not None and char == "*":
            gears.append((x, y))
    if start_pos is not None:
        number = int("".join(current_number))
        current_number = []
        numbers.append((number, start_pos))
        start_pos = None

parts = []
for number in numbers:
    number, start_pos = number
    x, y = start_pos
    length = len(str(number))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    adjacent = set()
    for y in range(y, y + length):
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                point = (new_x, new_y)
                adjacent.add(point)
    parts.append((number, adjacent))

gear_total = 0
for gear in gears:
    sets = []
    for number, adjacent in parts:
        if gear in adjacent:
            sets.append((number, adjacent))
    if len(sets) == 2:
        gear_total += sets[0][0] * sets[1][0]
print(gear_total)
