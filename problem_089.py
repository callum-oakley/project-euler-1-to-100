rules = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


def decode(roman):
    n = 0
    for numeral, value in rules:
        while roman.startswith(numeral):
            roman = roman[len(numeral) :]
            n += value
    return n


def encode(n):
    roman = ""
    for numeral, value in rules:
        while n >= value:
            n -= value
            roman += numeral
    return roman


def main():
    return sum(
        len(line.strip()) - len(encode(decode(line.strip())))
        for line in open("data/089").readlines()
    )
    # 743
