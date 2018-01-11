from functools import lru_cache

@lru_cache(maxsize=None)
def coinSums(pence, coins):
    if pence == 0:
        return [[]]
    return [
        coinSum + [coin]
        for coin in coins
        for coinSum in coinSums(pence - coin, frozenset(
            c for c in coins if c <= min(coin, pence - coin)
        ))
    ]

print(len(coinSums(200, frozenset({1, 2, 5, 10, 20, 50, 100, 200}))))
