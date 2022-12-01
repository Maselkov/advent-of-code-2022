from puzzleinput import lines

elves = []
current = 0
for line in lines:
    if line == "":
        elves.append(current)
        current = 0
        continue
    current += int(line)
elves.append(current)
total = sum(sorted(elves, reverse=True)[:3])
print(total)
