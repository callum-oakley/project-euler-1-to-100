def decode(cipher, password):
    result, i = "", 0
    for c in cipher:
        result += chr(c ^ password[i % len(password)])
        i += 1
    return result

cipher = [int(x) for x in open("data/059").read().strip().split(",")]
alphas = [x for x in range(ord("a"), ord("z") + 1)]
passwords = ((a, b, c) for a in alphas for b in alphas for c in alphas)
candidates = (decode(cipher, password) for password in passwords)
print(sum(ord(c) for c in max(candidates, key=lambda t: t.count("the"))))
