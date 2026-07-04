"""
A manufacturer of metal pistons finds that, on average, 12% of the
pistons they manufacture are rejected because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:
- No more than 2 rejects?
- At least 2 rejects?
"""


from math import comb


def binomial(n, x, p):
    return comb(n, x) * p**x * (1 - p) ** (n - x)


def main():
    percent, n = map(int, input().split())
    p = percent / 100

    no_more_than_2 = sum(binomial(n, x, p) for x in range(3))
    at_least_2 = sum(binomial(n, x, p) for x in range(2, n + 1))

    print(f"{no_more_than_2:.3f}")
    print(f"{at_least_2:.3f}")


if __name__ == "__main__":
    main()
