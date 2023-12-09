from puzzleinput import lines

histories = []
for line in lines:
    line = line.split()
    line = [int(x) for x in line]
    histories.append(line)

total = 0


def predict_number(hist: list[int]):
    new_sequence = []
    for i in range(len(hist) - 1):
        new_sequence.append(hist[i + 1] - hist[i])
    if new_sequence.count(0) == len(new_sequence):
        return hist[-1]
    return hist[-1] + predict_number(new_sequence)


for history in histories:
    total += predict_number(history)
print(total)
