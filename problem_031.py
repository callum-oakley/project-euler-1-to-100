from functools import cache


@cache
def coin_sums(pence, coins):
    if pence == 0:
        return [[]]
    return [
        coin_sum + [coin]
        for coin in coins
        for coin_sum in coin_sums(
            pence - coin,
            frozenset(c for c in coins if c <= min(coin, pence - coin)),
        )
    ]


def main():
    return len(coin_sums(200, frozenset({1, 2, 5, 10, 20, 50, 100, 200})))
    # 73682
