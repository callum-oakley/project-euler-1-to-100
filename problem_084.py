from random import randint


def main():
    i = 0
    visits = {n: 0 for n in range(40)}

    for j in range(10 ** 6):
        # Ignoring three consecutive double rule doesn't appear to affect the
        # result.
        i = (i + randint(1, 4) + randint(1, 4)) % 40

        if i == 30:  # G2J
            i = 10  # JAIL

        elif i == 2 or i == 17 or i == 33:  # CC
            card = randint(1, 16)
            if card == 1:
                i = 0  # GO
            elif card == 2:
                i = 10  # JAIL

        elif i == 7 or i == 22 or i == 36:  # CH
            card = randint(1, 16)
            if card == 1:
                i = 0  # GO
            elif card == 2:
                i = 10  # JAIL
            elif card == 3:
                i = 11  # C1
            elif card == 4:
                i = 24  # E3
            elif card == 5:
                i = 39  # H2
            elif card == 6:
                i = 5  # R1
            elif card == 7 or card == 8:
                while i != 5 and i != 15 and i != 25 and i != 35:  # R
                    i = (i + 1) % 40
            elif card == 9:
                while i != 12 and i != 28:  # U
                    i = (i + 1) % 40
            elif card == 10:
                i = (i - 3) % 40

        visits[i] += 1

    return "".join(
        f"{n:02}"
        for n in sorted(range(40), key=lambda i: visits[i], reverse=True)[:3]
    )
    # 101524
