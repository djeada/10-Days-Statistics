"""
A random variable, X, follows Poisson distribution with mean of λ.
Find the probability of X = k for the given values of λ and k.
"""

from math import exp, factorial


def poisson_probability(lam, k):
    return lam**k * exp(-lam) / factorial(k)


def main():
    lam = float(input())
    k = int(input())

    print(f"{poisson_probability(lam, k):.3f}")


if __name__ == "__main__":
    main()
