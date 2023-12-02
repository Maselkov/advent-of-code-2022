from puzzleinput import lines

total = 0
for line in lines:
    line = [x for x in line if x.isdigit()]
    total += int(line[0] + line[-1])
print(total)
