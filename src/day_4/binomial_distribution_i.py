"""
The ratio of boys to girls for babies born in Russia is 1.09:1.
If there is 1 child born per birth, what proportion of Russian families
with exactly 6 children will have at least  boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of  decimal places
(i.e., 1.234 format).
"""

from math import comb


def binomial(n, x, p):
    return comb(n, x) * p**x * (1 - p) ** (n - x)


def main():
    boys, girls = map(float, input().split())
    p_boy = boys / (boys + girls)

    result = sum(binomial(6, x, p_boy) for x in range(3, 7))

    print(f"{result:.3f}")


if __name__ == "__main__":
    main()
