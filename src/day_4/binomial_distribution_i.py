"""
The ratio of boys to girls for babies born in Russia is 1.09:1.
If there is 1 child born per birth, what proportion of Russian families
with exactly 6 children will have at least  boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of  decimal places
(i.e., 1.234 format).
"""


def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


def binomial(n, x, p):
    return (
        factorial(n) // factorial(n - x) // factorial(x) * (p ** x) * (1 - p) ** (n - x)
    )


def main():

    boys, girls = map(float, input().split())

    probability = boys / (boys + girls)

    result = (
        binomial(6, 3, probability)
        + binomial(6, 4, probability)
        + binomial(6, 5, probability)
        + binomial(6, 6, probability)
    )

    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
