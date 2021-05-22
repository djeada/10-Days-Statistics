"""
In a certain plant, the time taken to assemble a car is a random variable,X ,
having a normal distribution with a mean of 20 hours and a standard deviation of
2 hours. What is the probability that a car can be assembled at this plant in:
Less than 19.5 hours?
Between 20 and 22 hours?
"""

import math

pi = 3.14


def normal_distribution(x, miu, sigma):
    return math.exp(-(x - miu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * pi))


def cumulative_probability(x, miu, sigma):
    return 1 / 2 * (1 + math.erf((x - miu) / (sigma * math.sqrt(2))))


def main():

    miu, sigma = map(int, input().split())
    x = float(input())
    lower, upper = map(int, input().split())

    result = cumulative_probability(x, miu, sigma)
    print("{:.3f}".format(result))

    result = cumulative_probability(upper, miu, sigma) - cumulative_probability(
        lower, miu, sigma
    )
    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
