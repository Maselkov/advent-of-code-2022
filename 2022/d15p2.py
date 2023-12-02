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


def calculate_manhattan_distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


total = 0
max_coord = 20
min_coord = 0
multiply_by = 4000000


def find_all_points_with_certain_manhattan_distance(sensor, distance):
    points = []
    max_y = sensor[1] + distance + 1
    min_y = sensor[1] - distance - 1
    for y in range(min_y, max_y + 1):
        distance_to_center = abs(sensor[1] - y)
        left_x = sensor[0] - distance + 1 + distance_to_center
        right_x = sensor[0] + distance - 1 - distance_to_center
        if (
            left_x < min_coord
            or left_x > max_coord
            or right_x < min_coord
            or right_x > max_coord
        ):
            continue
        if y < min_coord or y > max_coord:
            continue
        if left_x == 14 or right_x == 14:
            if y == 11:
                print("WEH")
        weh_1 = check_if_point_is_in_range_of_any_beacon((left_x, y))
        weh_2 = check_if_point_is_in_range_of_any_beacon((right_x, y))
        # if weh_1 or weh_2:
        #     # print((left_x, y))
        #     # print((right_x, y))
        #     # print("WEHHH")
    return points


def check_if_point_is_in_range_of_any_beacon(point):
    for sensor in sensors:
        if (
            calculate_manhattan_distance(sensor["location"], point)
            <= sensor["distance"]
        ):
            return False
    return True


for i, sensor in enumerate(sensors):
    distance = calculate_manhattan_distance(sensor["location"], sensor["beacon"])
    sensors[i]["distance"] = distance
    sensors[i]["radius"] = distance
for sensor in sensors:
    points = find_all_points_with_certain_manhattan_distance(
        sensor["location"], sensor["distance"]
    )
    for point in points:
        if check_if_point_is_in_range_of_any_beacon(point):
            # check max and min
            if point[0] > max_coord:
                continue
            if point[0] < min_coord:
                continue
            if point[1] > max_coord:
                continue
            if point[1] < min_coord:
                continue
            print(point[0] * multiply_by + point[1])
            exit()

print(total)
