from puzzleinput import lines

part_2 = False
updates = []
rules = []
for line in lines:
    if not line:
        part_2 = True
        continue
    if part_2:
        updates.append([int(x) for x in line.split(",")])
    else:
        rules.append([int(x) for x in line.split("|")])

total = 0
for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                break
    else:
        total += update[len(update) // 2]

print(total)
