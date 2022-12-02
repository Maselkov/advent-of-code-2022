from puzzleinput import lines

score = 0
for line in lines:
    opponent, player = line.split(" ")
    opponent = ord(opponent) - ord("A") + 1
    player = ord(player) - ord("X") + 1
    score += player
    if opponent == player:
        score += 3
    else:
        if player == 1 and opponent == 3:
            score += 6
        if player == 2 and opponent == 1:
            score += 6
        if player == 3 and opponent == 2:
            score += 6

print(score)
