from puzzleinput import lines
import itertools

records = []
for line in lines:
    springs, arrangements = line.split(" ")
    arrangements = arrangements.split(",")
    arrangements = [int(x) for x in arrangements]
    records.append((springs, arrangements))

simplified = []
for springs, arrangements in records:
    springs = springs.split(".")
    springs = [x.rstrip(".").lstrip(".") for x in springs]
    springs = [x for x in springs if x]
    filtered = []
    for spring in springs:
        if spring.count("#") == len(spring):
            arrangements.remove(len(spring))
            continue
        filtered.append(spring)
    simplified.append((filtered, arrangements))
print(simplified)


def count_arrangements(sequence, arrangements):
    dp = [0] * (len(sequence) + 1)
    dp[0] = 1
    for i in range(1, len(sequence) + 1):
        for arrangement in arrangements:
            if arrangement <= i:
                dp[i] += dp[i - arrangement]
    return dp[len(sequence)]


print(count_arrangements("???", [1, 1]))
