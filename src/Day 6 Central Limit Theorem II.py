"""
The number of tickets purchased by each student for the University X vs.
University Y football game follows a distribution that has a mean of 2.4
and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase
last-minute tickets. If there are only 250 tickets left, what is the probability
that all 100 students will be able to purchase tickets?
"""

import math


def cumulativeProbability(x, miu, sigma):
    return 1 / 2 * (1 + math.erf((x - miu) / (sigma * math.sqrt(2))))


tickets = float(input())
students = int(input())
miu = float(input())
sigma = float(input())


print(
    "{:.4f}".format(
        cumulativeProbability(tickets, students * miu, math.sqrt(students) * sigma)
    )
)
