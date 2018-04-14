def digital_sum(n):
    return sum(int(d) for d in str(n))


print(max(digital_sum(a ** b) for a in range(100) for b in range(100)))
