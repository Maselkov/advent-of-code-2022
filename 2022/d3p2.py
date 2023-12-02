from puzzleinput import lines


total = 0
for i in range(0, len(lines), 3):
    group = [set(r) for r in lines[i : i + 3]]
    badge = group[0].intersection(group[1], group[2]).pop()
    code = ord(badge)
    if badge.islower():
        priority = code - ord("a") + 1
    else:
        priority = code - ord("A") + 27
    total += priority

print(total)
