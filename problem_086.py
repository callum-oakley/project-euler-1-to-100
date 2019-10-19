from math import sqrt, floor


count = 0
x = 1
while True:
    n = x + 1
    w_s = n ** 2 - x ** 2
    while w_s <= (2 * x) ** 2:
        w_s = n ** 2 - x ** 2
        w = round(sqrt(w_s))
        if w <= 2 * x and w ** 2 == w_s:
            count += floor(w / 2) - max(w - x - 1, 0)
            if count > 10 ** 6:
                print(x)
                exit()
        n += 1
    x += 1
