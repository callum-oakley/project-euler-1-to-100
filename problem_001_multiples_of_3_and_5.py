def sumOfMultiples(factors, n):
    return sum(x for x in range(n) if any(x % f == 0 for f in factors))

# sumOfMultiples({3, 5}, 1000) = 233168
