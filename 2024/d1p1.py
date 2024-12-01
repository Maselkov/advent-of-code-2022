from puzzleinput import lines

left = []
right = []
for line in lines:
    line = line.split()
    numbers = [int(x) for x in line]
    left.append(numbers[0])
    right.append(numbers[1])
left = sorted(left)
right = sorted(right)
total = 0
for x, y in zip(left, right):
    total += abs(x - y)
print(total)
