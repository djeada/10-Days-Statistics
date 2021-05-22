"""
A large elevator can transport a maximum of 9800 pounds. Suppose a load of
cargo containing 49 boxes must be transported via the elevator. The box weight
of this type of cargo follows a distribution with a mean of 205 pounds and a
standard deviation of 15 pounds. Based on this information, what is the
probability that all 49 boxes can be safely loaded into the freight elevator
and transported?
"""

import math


def cumulative_probability(x, miu, sigma):
    return 1 / 2 * (1 + math.erf((x - miu) / (sigma * math.sqrt(2))))


def main():

    maximum_load = float(input())
    n = int(input())
    miu = float(input())
    sigma = float(input())

    result = cumulative_probability(maximum_load, n * miu, math.sqrt(n) * sigma)
    print("{:.4f}".format(result))


if __name__ == "__main__":
    main()
