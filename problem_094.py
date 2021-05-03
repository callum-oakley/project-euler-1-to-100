# It is relatively straightforward by manipulation of expressions for the area
# of the triangle to show that all solutions are of the form
#
#     (2 * k - 1, 2 * k - 1, 2 * k) or (2 * k + 1, 2 * k + 1, 2 * k)
#
# for integer k, and that the "height" of the triangle along the line of
# symmetry is an integer. It follows then that solutions to the original problem
# correspond exactly with integer solutions to
#
#                        y ** 2 + k ** 2 = (2 * k +- 1) ** 2
#     <=> (3 * k +- 2) ** 2 - 3 * k ** 2 = 1
#
# which, letting x = (3 * k +- 2) is Pell's equation
#
#     x ** 2 - 3 * y ** 2 = 1
#
# Note that now not every integer solution x corresponds to an integer solution
# k, but every integer solution k does correspond to an integer solution x. We
# know how to calculate solutions to Pell's equation, so enumerating all
# solutions to Pell's equation and doing the reverse transformation will give us
# all solutions for k, and thus all almost equilateral triangles.


# https://en.wikipedia.org/wiki/Pell%27s_equation#Solutions
def pell_solutions(d, x1, y1):
    x, y = x1, y1
    while True:
        x, y = x1 * x + d * y1 * y, x1 * y + y1 * x
        yield x, y


def almost_equilateral_triangles():
    for x, y in pell_solutions(3, 2, 1):
        if (x + 2) % 3 == 0:
            k = (x + 2) // 3
            yield (2 * k - 1, 2 * k - 1, 2 * k)
        if (x - 2) % 3 == 0:
            k = (x - 2) // 3
            yield (2 * k + 1, 2 * k + 1, 2 * k)


sum = 0
for a, b, c in almost_equilateral_triangles():
    if a + b + c > 10 ** 9:
        break
    sum += a + b + c
print(sum)
# 518408346
