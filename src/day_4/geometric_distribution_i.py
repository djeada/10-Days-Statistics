"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""


def geometric(n, p):
    return p * (1 - p) ** (n - 1)


omega, space = map(int, input().split())
p = omega / space

n = int(input())

print("{:.3f}".format(geometric(n, p)))
