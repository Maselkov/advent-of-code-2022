from puzzleinput import lines

maximum = 0
current = 0
for line in lines:
    if line == "":
        current = 0
        continue
    current += int(line)
    if current > maximum:
        maximum = current
if current > maximum:
    maximum = current
print(maximum)
