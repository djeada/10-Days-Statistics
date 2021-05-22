"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""


def geometric(n, p):
    return p * (1 - p) ** (n - 1)


omega, space = map(int, input().split())
p = omega / space

n = int(input())

sum = 0
for i in range(1, 6):
    sum += geometric(i, p)

print("{:.3f}".format(sum))
