from puzzleinput import lines

cards = []
for line in lines:
    card, numbers = line.split(":")
    numbers = numbers.split("|")
    numbers = (
        set(int(num) for num in numbers[0].split()),
        set(int(num) for num in numbers[1].split()),
    )
    cards.append(numbers)

score = 0
for winning, owned in cards:
    card_worth = 0
    for number in owned:
        if number in winning:
            card_worth = 1 if not card_worth else card_worth * 2
    score += card_worth
print(score)
