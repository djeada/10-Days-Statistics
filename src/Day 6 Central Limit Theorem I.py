"""
A large elevator can transport a maximum of 9800 pounds. Suppose a load of
cargo containing 49 boxes must be transported via the elevator. The box weight
of this type of cargo follows a distribution with a mean of 205 pounds and a
standard deviation of 15 pounds. Based on this information, what is the
probability that all 49 boxes can be safely loaded into the freight elevator
and transported?
"""

import math


def cumulativeProbability(x, miu, sigma):
    return 1 / 2 * (1 + math.erf((x - miu) / (sigma * math.sqrt(2))))


maximumLoad = float(input())
n = int(input())
miu = float(input())
sigma = float(input())


print(
    "{:.4f}".format(cumulativeProbability(maximumLoad, n * miu, math.sqrt(n) * sigma))
)
