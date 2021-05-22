"""
In a certain plant, the time taken to assemble a car is a random variable,X ,
having a normal distribution with a mean of 20 hours and a standard deviation of
2 hours. What is the probability that a car can be assembled at this plant in:
Less than 19.5 hours?
Between 20 and 22 hours?
"""

import math

pi = 3.14


def normalDistribution(x, miu, sigma):
    return math.exp(-(x - miu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * pi))


def cumulativeProbability(x, miu, sigma):
    return 1 / 2 * (1 + math.erf((x - miu) / (sigma * math.sqrt(2))))


miu, sigma = map(int, input().split())
x = float(input())
lower, upper = map(int, input().split())


print("{:.3f}".format(cumulativeProbability(x, miu, sigma)))

print(
    "{:.3f}".format(
        cumulativeProbability(upper, miu, sigma)
        - cumulativeProbability(lower, miu, sigma)
    )
)
