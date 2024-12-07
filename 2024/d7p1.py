from puzzleinput import lines as lines
import operator
import itertools

data = []
for line in lines:
    result, numbers = line.split(": ")
    result = int(result)
    numbers = list(map(int, numbers.split()))
    data.append((result, numbers))


def evaluate(nums, oper):
    result = nums[0]
    for i, number in enumerate(nums[1:], 1):
        result = oper[i - 1](result, number)
    return result


operators = [operator.add, operator.mul]
total = 0
for result, numbers in data:
    operator_slots = len(numbers) - 1
    comb = itertools.product(operators, repeat=operator_slots)
    for ops in comb:
        if evaluate(numbers, ops) == result:
            total += result
            break
print(total)
