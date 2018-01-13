def value(card):
    return int(card[:2])

def suit(card):
    return card[2]

def straightFlush(hand):
    if flush(hand) and straight(hand):
        return "{:010}".format(value(hand[0]))

def fourOfAKind(hand):
    for i in [0, 1]:
        if len({value(hand[j]) for j in range(i, i + 4)}) == 1:
            return "{:010}".format(value(hand[i]))

def fullHouse(hand):
    if (
        value(hand[0]) == value(hand[1]) == value(hand[2]) and
        value(hand[3]) == value(hand[4])
    ):
        return "{:08}{:02}".format(value(hand[0]), value(hand[3]))
    if (
        value(hand[2]) == value(hand[3]) == value(hand[4]) and
        value(hand[0]) == value(hand[1])
    ):
        return "{:08}{:02}".format(value(hand[2]), value(hand[0]))

def flush(hand):
    s = suit(hand[0])
    for i in range(1, 5):
        if suit(hand[i]) != s:
            return
    return "".join("{:02}".format(value(card)) for card in hand)

def straight(hand):
    v0 = value(hand[0])
    for i in range(1, 5):
        if value(hand[i]) != v0 - i:
            return
    return "{:010}".format(v0)

def threeOfAKind(hand):
    for i in range(3):
        if value(hand[i]) == value(hand[i + 1]) == value(hand[i + 2]):
            return "{:010}".format(value(hand[i]))

def twoPair(hand):
    for i in range(4):
        if value(hand[i]) == value(hand[i + 1]):
            for j in range(i + 2, 4):
                if value(hand[j]) == value(hand[j + 1]):
                    return "{:08}{:02}".format(value(hand[i]), value(hand[j]))

def onePair(hand):
    for i in range(4):
        if value(hand[i]) == value(hand[i + 1]):
            return "{:010}".format(value(hand[i]))

def rank(hand):
    v = straightFlush(hand)
    if v:
        return (8, v)
    v = fourOfAKind(hand)
    if v:
        return (7, v)
    v = fullHouse(hand)
    if v:
        return (6, v)
    v = flush(hand)
    if v:
        return (5, v)
    v = straight(hand)
    if v:
        return (4, v)
    v = threeOfAKind(hand)
    if v:
        return (3, v)
    v = twoPair(hand)
    if v:
        return (2, v)
    v = onePair(hand)
    if v:
        return (1, v)
    return (0, 0)

def score(hand):
    hand.sort(reverse=True)
    r, v = rank(hand)
    return "{}-{}-{}".format(r, v, "".join(hand))

special = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def parse(f):
    if f[0] in special:
        value = special[f[0]]
    else:
        value = int(f[0])
    return "{:02}{}".format(value, f[1])

wins = 0
for line in open("data/054").read().splitlines():
    cards = [parse(f) for f in line.split()]
    wins += 1 if score(cards[:5]) > score(cards[5:]) else 0
print(wins)
