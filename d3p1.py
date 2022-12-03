from puzzleinput import lines


total = 0
for rucksack in lines:
    half = len(rucksack) // 2
    first, second = set(rucksack[:half]), set(rucksack[half:])
    intersection = first.intersection(second)
    for item in intersection:
        code = ord(item)
        if item.islower():
            priority = code - ord("a") + 1
        else:
            priority = code - ord("A") + 27
        total += priority

print(total)
