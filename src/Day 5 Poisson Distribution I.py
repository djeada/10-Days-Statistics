"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""

e = 2.718281828459


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def poisson(l, k):
    return l ** k * e ** (-l) / factorial(k)


l = float(input())
k = int(input())

print("{:.3f}".format(poisson(l, k)))
