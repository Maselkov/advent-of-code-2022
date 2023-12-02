from puzzleinput import lines
import math

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
        for draw in result:
            count, item = draw.split(" ")
            count = int(count)
            subdraw.append((count, item))
        draws.append(subdraw)
    games.append(draws)


total = 0
for game_id, game in enumerate(games, start=1):
    max_color = {"red": 0, "green": 0, "blue": 0}
    for draw in game:
        for count, item in draw:
            if count > max_color[item]:
                max_color[item] = count
    total += math.prod(max_color.values())
print(total)
