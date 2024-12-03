import re
from puzzleinput import lines

pattern = r"do(?!n't)(.*?)(?=don't)"
total = 0
line = "".join(lines)
line = "do" + line + "don't"
matches = re.findall(pattern, line)
for match in matches:
    for inner_match in re.findall(r"mul\(\d+,\d+\)", match):
        a, b = map(int, re.findall(r"\d+", inner_match))
        total += a * b

print(total)
