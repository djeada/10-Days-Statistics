"""
The final grades for a Physics exam taken by a large group
of students have a mean of 70 and a standard deviation of 10.
If we can approximate the distribution of these grades by
a normal distribution, what percentage of the students:

Scored higher than 80 (i.e., have a grade > 80)?
Passed the test (i.e., have a grade >= 60)?
Failed the test (i.e., have a grade < 60)?
Find and print the answer to each question on a new line,
rounded to a scale of 2 decimal places.
"""
import math

pi = 3.14


def normalDistribution(x, miu, sigma):
    return math.exp(-(x - miu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * pi))


def cumulativeProbability(x, miu, sigma):
    return 1 / 2 * (1 + math.erf((x - miu) / (sigma * math.sqrt(2))))


miu, sigma = map(int, input().split())
x1 = float(input())
x2 = float(input())

print("{:.2f}".format((100 - cumulativeProbability(x1, miu, sigma) * 100)))
print("{:.2f}".format((100 - cumulativeProbability(x2, miu, sigma) * 100)))
print("{:.2f}".format(cumulativeProbability(x2, miu, sigma) * 100))
