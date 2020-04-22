from math import sqrt, ceil


def attempt_sub(word, square):
    square = str(square)
    sub = {}
    for i in range(len(word)):
        if (
            # can't map one letter to two digits
            word[i] in sub
            and sub[word[i]] != square[i]
            # can't map two letters to the same digit
            or word[i] not in sub
            and square[i] in sub.values()
        ):
            return
        else:
            sub[word[i]] = square[i]
    return sub


def apply_sub(sub, word):
    return int("".join(sub[letter] for letter in word))


def anagrams(words):
    for j in range(len(words)):
        for i in range(j):
            a, b = words[i], words[j]
            if sorted(a) == sorted(b):
                yield (a, b)


squares_by_length = {
    i: [n ** 2 for n in range(ceil(sqrt(10 ** (i - 1))), ceil(sqrt(10 ** i)))]
    for i in range(1, 10)
}

words = [w.strip('"') for w in open("data/098").read().split(",")]

max_anagramic_square = 0
for a, b in anagrams(words):
    for square in squares_by_length[len(a)]:
        sub = attempt_sub(a, square)
        if sub:
            b_sub = apply_sub(sub, b)
            # implicitly checks that the substitution didn't start with a 0
            # because b_sub would be a different length if it did
            if b_sub in squares_by_length[len(a)]:
                max_anagramic_square = max(max_anagramic_square, square, b_sub)

print(max_anagramic_square)
