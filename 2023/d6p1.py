from puzzleinput import lines

races = []
times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]
races = list(zip(times, distances))

total = 1
for time, record in races:
    speed = 0
    ways_to_win = 0
    for ms in range(time + 1):
        potential_distance = speed * (time - ms)
        if potential_distance > record:
            ways_to_win += 1
        speed += 1
    total *= ways_to_win
print(total)
