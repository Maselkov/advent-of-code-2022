from puzzleinput import lines

numbers = []
for line in lines:
    line = line.split()
    numbers.append([int(x) for x in line])


def try_problem(line):
    decreasing = True
    increasing = True
    for i in range(1, len(line)):
        number = line[i]
        if number < line[i - 1]:
            decreasing = False
        if number > line[i - 1]:
            increasing = False
        if not decreasing and not increasing:
            break
        if not 1 <= abs(number - line[i - 1]) <= 3:
            break
    else:
        return True


total = 0
for line in numbers:
    if try_problem(line):
        total += 1
    else:
        for i in range(len(line)):
            if try_problem(line[:i] + line[i + 1 :]):
                total += 1
                break
print(total)
