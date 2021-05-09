from problem_016 import digit_sum


def main():
    return max(digit_sum(a ** b) for a in range(100) for b in range(100))
    # 972
