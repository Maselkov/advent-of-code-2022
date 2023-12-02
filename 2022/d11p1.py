from puzzleinput import lines
from collections import deque


class Monkey:
    def __init__(self) -> None:
        self.inventory = deque()
        self.test_value = None
        self.operation = None
        self.on_true = None
        self.on_false = None
        self.inspected_items = 0


monkeys = []
i = 0
temp_monkey = Monkey()
for line in lines:
    line = line.strip()
    if not line:
        monkeys.append(temp_monkey)
        i += 1
        temp_monkey = Monkey()
        continue
    if line.startswith("Monkey"):
        continue
    elif line.startswith("Starting items"):
        items = line.split()[2:]
        for item in items:
            item = item.strip(",")
            item = int(item)
            temp_monkey.inventory.append(item)
    elif line.startswith("Operation"):
        items = line.split()[1:]
        operation = items[3]
        operand = items[4]
        if operand.isdigit():
            operand = int(operand)
        if operation == "+" and operand == "old":
            temp_monkey.operation = lambda old: old + old
        elif operation == "+":
            temp_monkey.operation = (lambda o: lambda old: old + o)(operand)
        elif operation == "*" and operand == "old":
            temp_monkey.operation = lambda old: old * old
        elif operation == "*":
            temp_monkey.operation = (lambda o: lambda old: old * o)(operand)
    elif line.startswith("Test"):
        items = line.split()
        temp_monkey.test_value = int(items[3])
    elif line.startswith("If true"):
        items = line.split()
        temp_monkey.on_true = int(items[5])
    elif line.startswith("If false"):
        items = line.split()
        temp_monkey.on_false = int(items[5])

monkeys.append(temp_monkey)
rounds = 20
for _ in range(rounds):
    for monkey in monkeys:
        while monkey.inventory:
            item = monkey.inventory.popleft()
            monkey.inspected_items += 1
            worry_level = monkey.operation(item)
            worry_level = worry_level // 3
            if worry_level % monkey.test_value == 0:
                thrown_to = monkey.on_true
            else:
                thrown_to = monkey.on_false
            monkeys[thrown_to].inventory.append(worry_level)

totals = sorted((m.inspected_items for m in monkeys), reverse=True)
print(totals[0] * totals[1])
