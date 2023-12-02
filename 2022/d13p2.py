from puzzleinput import lines
from collections import deque
from copy import deepcopy
import ast


class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __lt__(self, other):
        return compare_values(deepcopy(self.packet), deepcopy(other.packet)) == 1

    def __eq__(self, other):
        return compare_values(deepcopy(self.packet), deepcopy(other.packet)) == 0


packets = []
for line in lines:
    if not line:
        continue
    packet = ast.literal_eval(line)
    packets.append(Packet(packet))
dividers = [Packet(d) for d in [[[2]], [[6]]]]
packets.extend(dividers)


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


decoder_key = 1
packets = sorted(packets)
for packet in packets:
    if packet in dividers:
        decoder_key *= packets.index(packet) + 1
print(decoder_key)
