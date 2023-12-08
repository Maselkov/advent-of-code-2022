from puzzleinput import lines
import math

sequence = lines[0].replace("L", "0").replace("R", "1")
sequence = [int(x) for x in sequence]
network = {}
for line in lines[2:]:
    line = line.split(" = ")
    connects_to = line[1][1:-1].split(", ")
    network[line[0]] = connects_to
current_nodes = [node for node in network if node.endswith("A")]
steps_needed = []
for node in current_nodes:
    steps = 0
    while True:
        for step in sequence:
            steps += 1
            node = network[node][step]
            if node.endswith("Z"):
                steps_needed.append(steps)
                break
        else:
            continue
        break
result = math.lcm(*steps_needed)
print(result)
