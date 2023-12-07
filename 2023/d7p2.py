from puzzleinput import lines

values = "J23456789TQKA"
hands_and_bids = []
for line in lines:
    line = line.split()
    hand = list(line[0])
    for i in range(len(hand)):
        hand[i] = values.index(hand[i])
    bid = int(line[1])
    hands_and_bids.append((hand, bid))


def is_five_of_a_kind(hand):
    for i in range(1, len(values)):
        temp_hand = [i if card == 0 else card for card in hand]
        if temp_hand.count(i) == 5:
            return True
    return False


def is_four_of_a_kind(hand):
    for i in range(1, len(values)):
        temp_hand = [i if card == 0 else card for card in hand]
        if temp_hand.count(i) == 4:
            return True
    return False


def is_full_house(hand):
    for i in range(1, len(values)):
        temp_hand = [i if card == 0 else card for card in hand]
        if temp_hand.count(i) == 3:
            for j in range(1, len(values)):
                if i != j and temp_hand.count(j) >= 2:
                    return True
    return False


def is_three_of_a_kind(hand):
    for i in range(1, len(values)):
        temp_hand = [i if card == 0 else card for card in hand]
        if temp_hand.count(i) == 3:
            return True
    return False


def is_two_pairs(hand):
    pairs = 0
    for i in range(1, len(values)):
        temp_hand = [i if card == 0 else card for card in hand]
        if temp_hand.count(i) == 2:
            pairs += 1
    return pairs == 2


def is_one_pair(hand):
    for i in range(1, len(values)):
        temp_hand = [i if card == 0 else card for card in hand]
        if temp_hand.count(i) == 2:
            return True
    return False


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.strength = 0
        self.high_card = 0
        self.bid = 0
        self.calculate_strength()

    def calculate_strength(self):
        if is_five_of_a_kind(self.hand):
            self.strength = 6
            self.high_card = max(self.hand)
        elif is_four_of_a_kind(self.hand):
            self.strength = 5
            self.high_card = max(self.hand)
        elif is_full_house(self.hand):
            self.strength = 4
            self.high_card = max(self.hand)
        elif is_three_of_a_kind(self.hand):
            self.strength = 3
            self.high_card = max(self.hand)
        elif is_two_pairs(self.hand):
            self.strength = 2
            self.high_card = max(self.hand)
        elif is_one_pair(self.hand):
            self.strength = 1
            self.high_card = max(self.hand)
        else:
            self.strength = 0
            self.high_card = max(self.hand)

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        elif self.strength == other.strength:
            for i in range(len(self.hand)):
                if self.hand[i] > other.hand[i]:
                    return True
                elif self.hand[i] < other.hand[i]:
                    return False
        else:
            return False

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        elif self.strength == other.strength:
            for i in range(len(self.hand)):
                if self.hand[i] < other.hand[i]:
                    return True
                elif self.hand[i] > other.hand[i]:
                    return False
        else:
            return False

    def __eq__(self, other):
        if self.strength == other.strength:
            for i in range(len(self.hand)):
                if self.hand[i] != other.hand[i]:
                    return False
            return True
        return False


hands = []
for hand, bid in hands_and_bids:
    hand = Hand(hand)
    hand.bid = bid
    hands.append(hand)

total_winnings = 0
for i, hand in enumerate(sorted(hands), start=1):
    total_winnings += i * hand.bid

print(total_winnings)
