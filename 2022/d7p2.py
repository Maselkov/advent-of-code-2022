from puzzleinput import lines

wd = ""
required_size = 30000000
total = 0

sizes = []


def calculate_size(tree, path):
    global total
    dir_size = 0
    for key, value in tree.items():
        if key == "..":
            continue
        if isinstance(value, int):
            dir_size += value
        else:
            dir_size += calculate_size(value, key)
    sizes.append(dir_size)
    return dir_size


tree = {"/": {}}
current = tree
for line in lines:
    if line.startswith("$"):
        args = line[2:].split()
        command, arguments = args[0], args[1:]
        match command:
            case "cd":
                current = current[arguments[0]]
    else:
        size, name = line.split()
        if size == "dir":
            size = {"..": current}
        else:
            size = int(size)
        current[name] = size
size_cache = {}

calculate_size(tree["/"], "/")
lowest_size = float("inf")
unused = 70000000 - max(sizes)
for size in sizes:
    if size + unused >= required_size:
        if size < lowest_size:
            lowest_size = size
print(lowest_size)
