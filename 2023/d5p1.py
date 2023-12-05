from puzzleinput import lines

maps = []
seeds = []
current_map = []

for line in lines:
    if line == "":
        if current_map != []:
            maps.append(current_map)
            current_map = []
        continue
    if line.startswith("seeds: "):
        seeds = list(map(int, line[7:].split(" ")))
        continue
    if "map" in line:
        continue
    numbers = list(map(int, line.split(" ")))
    current_map.append(numbers)
maps.append(current_map)

lowest = float("inf")
for seed in seeds:
    for mapping in maps:
        for line in mapping:
            if line[1] <= seed < line[1] + line[2]:
                diff = seed - line[1]
                seed = diff + line[0]
                break
    if seed < lowest:
        lowest = seed
print(lowest)
