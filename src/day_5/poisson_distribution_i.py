"""
A random variable, X, follows Poisson distribution with mean of λ.
Find the probability of X = k for the given values of λ and k.
"""

e = 2.718281828459


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def poisson(l, k):
    return l ** k * e ** (-l) / factorial(k)


def main():

    l = float(input())
    k = int(input())

    result = poisson(l, k)
    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
