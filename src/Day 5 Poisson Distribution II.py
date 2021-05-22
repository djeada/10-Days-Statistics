"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""


def E(l):
    return l + l ** 2


l1, l2 = map(float, input().split())

print("{:.3f}".format(160 + 40 * E(l1)))
print("{:.3f}".format(128 + 40 * E(l2)))
