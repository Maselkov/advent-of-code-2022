from puzzleinput import lines

histories = []
for line in lines:
    line = line.split()
    line = [int(x) for x in line]
    histories.append(line)

total = 0


def predict_number(hist: list[int]):
    new_sequence = []
    for i in range(1, len(hist)):
        new_sequence.append(hist[i] - hist[i - 1])
    if new_sequence.count(0) == len(new_sequence):
        return hist[0]
    result = predict_number(new_sequence)
    return hist[0] - result


for history in histories:
    total += predict_number(history)
print(total)
