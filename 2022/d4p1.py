from puzzleinput import lines


def contains(r1, r2):
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        return True
    return False


total = 0
for pairs in lines:
    pairs = pairs.split(",")
    pairs = [[int(x) for x in pair.split("-")] for pair in pairs]
    if contains(pairs[0], pairs[1]) or contains(pairs[1], pairs[0]):
        total += 1
print(total)
