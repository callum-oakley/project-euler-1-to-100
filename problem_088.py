from functools import lru_cache


@lru_cache(maxsize=None)
def factorisations(n):
    res = [[n]]
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            res += [[d] + f for f in factorisations(n // d) if f[0] >= d]
        d += 1
    return res


# Returns the k for which n is a product-sum number (though not necessaily a
# minimal product sum number).
def possible_k(n):
    return {n - sum(f) + len(f) for f in factorisations(n) if len(f) > 1}


# For a given k, 2 * k is always a product-sum number, since
# 1 + ... + 1 + 2 + k = k - 2 + 2 + k = 2 * k = 1 * ... * 1 * 2 * k
# so the minimal product sum will be at most 2 * k. In our search below then, we
# need not consider n > 2 * max_k.
def minimal_product_sums(max_k):
    minimal_product_sums = {}
    for n in range(2, max_k * 2 + 1):
        for k in possible_k(n):
            if k <= max_k and k not in minimal_product_sums:
                minimal_product_sums[k] = n
    return set(minimal_product_sums.values())


print(sum(minimal_product_sums(12000)))
# 7587457
