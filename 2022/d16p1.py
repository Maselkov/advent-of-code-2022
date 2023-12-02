from puzzleinput import lines

valves = {}

for line in lines:
    line = line.strip("Valve ")
    valve_name = line[:2]
    part_1, part_2 = line.split("; ")
    flow_rate = int(part_1.split("=")[1])
    leads_to = part_2.split()[4:]
    leads_to = [valve.strip(",") for valve in leads_to]
    valves[valve_name] = {"flow_rate": flow_rate, "leads_to": leads_to}


def get_maximum_possible_flow(valve_name, minutes_left):
    valve = valves[valve_name]
    flow_rate = valve["flow_rate"]
    leads_to = valve["leads_to"]
    minutes_left -= 1
    if minutes_left == 0:
        return flow_rate
    else:
        return flow_rate + max(
            [get_maximum_possible_flow(valve, minutes_left) for valve in leads_to]
        )


get_maximum_possible_flow("AA", 30)
print(valves)
