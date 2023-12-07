from puzzleinput import lines

races = []
time = int("".join(lines[0].split()[1:]))
record = int("".join(lines[1].split()[1:]))

total = 1
speed = 0
ways_to_win = 0
for ms in range(time + 1):
    potential_distance = speed * (time - ms)
    if potential_distance > record:
        ways_to_win += 1
    speed += 1
    if ms % (time // 10) == 0:
        print(f"{ms / time * 100:.0f}%")
total *= ways_to_win
print(total)
