from puzzleinput import lines

cards = {}
for i, line in enumerate(lines, start=1):
    card, numbers = line.split(":")
    numbers = numbers.split("|")
    numbers = (
        set(int(num) for num in numbers[0].split()),
        set(int(num) for num in numbers[1].split()),
    )
    matches = 0
    for number in numbers[1]:
        if number in numbers[0]:
            matches += 1
    cards[i] = {
        "owned": numbers[1],
        "winning": numbers[0],
        "count": 1,
        "matches": matches,
    }

for i in cards:
    card = cards[i]
    for j in range(1, card["matches"] + 1):
        cards[i + j]["count"] += 1 * card["count"]

total_amount_of_cards = sum(card["count"] for card in cards.values())
print(total_amount_of_cards)
