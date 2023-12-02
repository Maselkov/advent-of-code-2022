from puzzleinput import lines

games = []
for line in lines:
    line = line[5:]
    game_id, results = line.split(": ")
    game_id = int(game_id)
    results = results.split("; ")
    draws = []
    for result in results:
        subdraw = []
        result = result.split(", ")
        print(result)
        for draw in result:
            count, item = draw.split(" ")
            count = int(count)
            subdraw.append((count, item))
        draws.append(subdraw)
    games.append(draws)

invalid_games = []
limits = {"red": 12, "green": 13, "blue": 14}
for game_id, game in enumerate(games, start=1):
    for draw in game:
        for count, item in draw:
            if count > limits[item]:
                invalid_games.append(game_id)
                break
        else:
            continue
        break
print(sum(range(len(games) + 1)) - sum(invalid_games))
