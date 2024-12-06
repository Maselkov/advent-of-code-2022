import sys
from os import path

with open(f"2024/inputs/{path.basename(sys.argv[0])[:-5]}.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    numbers = [int(line) for line in lines if line.isdigit()]
try:
    with open(f"2024/inputs/{path.basename(sys.argv[0])[:-5]}-ex.txt") as f:
        elines = [line.rstrip() for line in f.readlines()]
        enumbers = [int(line) for line in lines if line.isdigit()]
except FileNotFoundError:
    pass
