from puzzleinput import lines
from collections import deque

size = 4
signal = lines[0]
buffer = deque(maxlen=size)
for index, character in enumerate(signal, 1):
    buffer.append(character)
    if len(buffer) == size:
        if len(set(buffer)) == size:
            print(index)
            break
