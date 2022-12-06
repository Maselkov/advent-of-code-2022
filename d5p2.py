from collections import defaultdict, deque
from puzzleinput import lines

stacks = defaultdict(deque)

total = 0

for index, line in enumerate(lines):
    if line.startswith(" 1"):
        break
    for count, i in enumerate(range(1, len(line), 4), 1):
        if line[i] == " ":
            continue
        stacks[count].appendleft(line[i])
for command in lines[index + 2 :]:
    numbers = [int(s) for s in command.split() if s.isdigit()]
    stack = []
    for _ in range(numbers[0]):
        stack.append(stacks[numbers[1]].pop())
    stack.reverse()
    for item in stack:
        stacks[numbers[2]].append(item)
message = ""
for i in range(1, max(stacks.keys()) + 1):
    message += stacks[i].pop()
print(message)
