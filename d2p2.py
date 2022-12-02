from puzzleinput import lines

score = 0
for line in lines:
    opponent, condition = line.split(" ")
    opponent = ord(opponent) - ord("A") + 1
    if condition == "Y":
        score += opponent + 3
    elif condition == "Z":
        score += 6
        if opponent == 1:
            score += 2
        if opponent == 2:
            score += 3
        if opponent == 3:
            score += 1
    elif condition == "X":
        if opponent == 1:
            score += 3
        if opponent == 2:
            score += 1
        if opponent == 3:
            score += 2


print(score)
