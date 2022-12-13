from puzzleinput import lines
from collections import deque
import ast

packet_pairs = []
pair = []
for line in lines:
    if not line:
        packet_pairs.append(pair)
        pair = []
        continue
    packet = ast.literal_eval(line)
    pair.append(packet)
packet_pairs.append(deque(pair))


def compare_values(left, right):
    if type(left) == int == type(right):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    elif type(left) == list == type(right):
        while left and right:
            value_left = left.pop(0)
            value_right = right.pop(0)
            result = compare_values(value_left, value_right)
            if result != 0:
                return result
        if left and not right:
            return -1
        elif right and not left:
            return 1
        else:
            return 0
    else:
        if not type(left) == list:
            left = [left]
        else:
            right = [right]
        return compare_values(left, right)


indices_sum = 0
for index, pair in enumerate(packet_pairs, start=1):
    left, right = tuple(pair)
    if compare_values(left, right) == 1:
        print(index)
        indices_sum += index
print(indices_sum)
