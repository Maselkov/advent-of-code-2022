from puzzleinput import lines

wd = ""
max_size = 100000
total = 0


def calculate_size(tree, path):
    global total
    dir_size = 0
    for key, value in tree.items():
        if key == "..":
            continue
        if isinstance(value, int):
            dir_size += value
        else:
            dir_size += calculate_size(value, path + key)
    if dir_size <= max_size:
        total += dir_size
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
print(total)
