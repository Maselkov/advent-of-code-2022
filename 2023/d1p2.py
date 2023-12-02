from puzzleinput import lines

valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
for line in lines:
    numbers = []
    for i, character in enumerate(line):
        if character.isalpha():
            for digit in valid_digits:
                if line[i : i + len(digit)] == digit:
                    numbers.append(str(valid_digits.index(digit) + 1))
                    break
        else:
            numbers.append(character)
    new_line = [x for x in line if x.isdigit()]
    total += int(numbers[0] + numbers[-1])
print(total)
