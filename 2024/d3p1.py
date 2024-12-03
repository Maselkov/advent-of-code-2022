import re
from puzzleinput import lines

total = 0
for line in lines:
    for match in re.findall(r"mul\(\d+,\d+\)", line):
        a, b = map(int, re.findall(r"\d+", match))
        total += a * b
print(total)
