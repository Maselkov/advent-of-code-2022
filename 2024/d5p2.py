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


def is_correct(update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


incorrect_updates = []

for update in updates:
    if not is_correct(update):
        incorrect_updates.append(update)


def correct_update(update):
    new_update = update.copy()
    for rule in rules:
        if rule[0] in new_update and rule[1] in new_update:
            if new_update.index(rule[0]) > new_update.index(rule[1]):
                new_update.remove(rule[1])
                new_update.insert(new_update.index(rule[0]) + 1, rule[1])
    return new_update


updates = incorrect_updates

while updates:
    to_correct = []
    for update in updates:
        if is_correct(update):
            total += update[len(update) // 2]
        else:
            to_correct.append(correct_update(update))
    updates = to_correct
print(total)
