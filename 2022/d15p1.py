from puzzleinput import lines


sensors = []
beacons = {}

for line in lines:
    line = line.split(": ")
    line = [item.split("x=")[1] for item in line]
    line = [item.replace("y=", "") for item in line]
    line = [item.split(", ") for item in line]
    line = [[int(item) for item in item] for item in line]
    sensor, beacon = line
    sensors.append({"location": tuple(sensor), "beacon": tuple(beacon)})
print(sensors)


def calculate_manhattan_distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


total = 0
total_y_10 = 0

sought_y = 2000000


def calculate_number_of_points_lower_than_manhattan_distance(sensor, distance):
    global total
    y = sought_y
    for x in range(sensor[0] - distance, sensor[0] + distance + 1):
        if (x, y) not in beacons:
            if abs(x - sensor[0]) + abs(y - sensor[1]) <= distance:
                beacons[(x, y)] = distance
                if y == sought_y:
                    total += 1


for sensor in sensors:
    distance = calculate_manhattan_distance(sensor["location"], sensor["beacon"])
    beacons[sensor["beacon"]] = distance
    points = calculate_number_of_points_lower_than_manhattan_distance(
        sensor["location"], distance
    )
print(total)
