"""
A manufacturer of metal pistons finds that, on average, 12% of the
pistons they manufacture are rejected because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
"""


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def binomial(n, x, p):
    return (
        factorial(n)
        // (factorial(n - x) * factorial(x))
        * (p ** x)
        * (1 - p) ** (n - x)
    )


p, n = map(int, input().split())
p /= 100

print("{:.3f}".format(binomial(n, 0, p) + binomial(n, 1, p) + binomial(n, 2, p)))

sum = 0
for i in range(2, n + 1):
    sum += binomial(n, i, p)

print("{:.3f}".format(sum))
