from puzzleinput import lines

left = []
right = []
for line in lines:
    line = line.split()
    numbers = [int(x) for x in line]
    left.append(numbers[0])
    right.append(numbers[1])
total = 0
for number in left:
    total += number * right.count(number)
print(total)
