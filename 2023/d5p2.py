from puzzleinput import lines
import sys

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
    numbers = {
        "offset": numbers[0] - numbers[1],
        "start": numbers[1],
        "length": numbers[1],
        "end": numbers[1] + numbers[2],
    }
    current_map.append(numbers)
maps.append(current_map)

for mapping in maps:
    mapping.sort(key=lambda x: x["start"])

seeds = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]


lowest = float("inf")
ranges_and_offsets = []

for mapping in maps:
    level = []
    if mapping[0]["start"] != 0:
        level.append((range(0, mapping[0]["start"]), 0))
    for i, line in enumerate(mapping):
        level.append((range(line["start"], line["end"]), line["offset"]))
        if i + 1 < len(mapping):
            if line["end"] != mapping[i + 1]["start"]:
                level.append((range(line["end"], mapping[i + 1]["start"]), 0))
    level.append((range(mapping[-1]["end"], sys.maxsize), 0))
    merged = []
    for i, line in enumerate(level):
        if i == 0:
            merged.append(line)
            continue
        if line[1] == merged[-1][1]:
            merged[-1] = (range(merged[-1][0].start, line[0].stop), line[1])
        else:
            merged.append(line)

    ranges_and_offsets.append(merged)


def process_seed_range(start, length, level):
    global lowest
    end = start + length
    ranges = ranges_and_offsets[level]
    clamped = ranges[:]
    for j, (range_, offset) in enumerate(ranges):
        if start in range_:
            clamped[j] = (range(start, range_.stop), offset)
            clamped = clamped[j:]
            break
    for j, (range_, offset) in enumerate(clamped):
        if end in range_:
            clamped[j] = (range(range_.start, end), offset)
            clamped = clamped[: j + 1]
            break
    print(clamped)
    new_seed_ranges = []
    for range_, offset in clamped:
        new_seed_ranges.append((range_.start + offset, range_.stop - range_.start))
    print(new_seed_ranges)
    if level == len(ranges_and_offsets) - 1:
        for range_ in new_seed_ranges:
            if range_[0] < lowest:
                lowest = range_[0]
        return
    for seed_range in new_seed_ranges:
        process_seed_range(*seed_range, level + 1)


for sr in seeds:
    process_seed_range(*sr, 0)
print(lowest)
