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
total = 0
op_cycles_left = 1
op = ("noop",)
for cycle in range(221):
    if cycle in (20, 60, 100, 140, 180, 220):
        signal_strength = cycle * x
        total += signal_strength
    op_cycles_left -= 1
    if op_cycles_left == 0:
        if op[0] == "addx":
            x += op[1]
        instruction = instructions.popleft()
        match instruction[0]:
            case "noop":
                op = instruction
                op_cycles_left = 1
            case "addx":
                op = instruction
                op_cycles_left = 2
print(total)
