"""
You have a sample of 100 values from a population with mean 500 and with
standard deviation 80. Compute the interval that covers the middle 95% of the
distribution of the sample mean; in other words, compute A and B such that
P(A < x < B). Use the value of z = 1.96. Note that z is the z-score.
"""

import math


def main():
    n = int(input())
    miu = float(input())
    sigma = float(input())
    percent = float(input())
    z = float(input())

    e = z * sigma / math.sqrt(n)
    print("{:2f}".format(miu - e))
    print("{:2f}".format(miu + e))


if __name__ == "__main__":
    main()
