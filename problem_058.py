from problem_027 import is_prime


def main():
    total = 13
    prime = 8
    side_len = 7
    while prime / total >= 0.1:
        side_len += 2
        total += 4
        for k in range(1, 4):
            prime += 1 if is_prime(side_len ** 2 - k * (side_len - 1)) else 0
    return side_len
    # 26241
