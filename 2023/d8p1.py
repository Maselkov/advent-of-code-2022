from puzzleinput import lines

sequence = lines[0].replace("L", "0").replace("R", "1")
sequence = [int(x) for x in sequence]
network = {}
for line in lines[2:]:
    line = line.split(" = ")
    connects_to = line[1][1:-1].split(", ")
    network[line[0]] = connects_to
steps = 0
current_node = "AAA"
while True:
    for step in sequence:
        steps += 1
        current_node = network[current_node][step]
        if current_node == "ZZZ":
            print(steps)
            exit()
