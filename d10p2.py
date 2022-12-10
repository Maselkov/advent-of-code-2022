from puzzleinput import lines
from collections import deque

x = 1
ops = []
instructions = deque()
for instruction in lines:
    instruction = instruction.split()
    if len(instruction) == 1:
        instruction = (instruction[0],)
    else:
        instruction = (instruction[0], int(instruction[1]))
    instructions.append(instruction)
op_cycles_left = 1
op = ("noop",)

for cycle in range(240):
    if not cycle % 40:
        print()

    op_cycles_left -= 1
    proceed = False
    if op_cycles_left == 0:
        if op[0] == "addx":
            x += op[1]
        proceed = True
    pixel_position = cycle % 40
    sprite_positions = (x - 1, x, x + 1)
    if pixel_position in sprite_positions:
        print("█", end="")
    else:
        print(" ", end="")
    if proceed:
        instruction = instructions.popleft()
        match instruction[0]:
            case "noop":
                op = instruction
                op_cycles_left = 1
            case "addx":
                op = instruction
                op_cycles_left = 2
