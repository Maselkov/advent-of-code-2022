import sys
from os import path
with open(f"inputs/{path.basename(sys.argv[0])[:-5]}.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    numbers = [int(line) for line in lines if line.isdigit()]
