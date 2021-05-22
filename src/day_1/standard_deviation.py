"""
Given an array, X, of N integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the
standard deviation.
"""

import math


def getMean(data):
    n = len(data)
    sum = 0
    for x in data:
        sum += x
    return sum / n


def getStandardDev(data):
    n = len(data)
    sum = 0
    mean = getMean(data)
    for x in data:
        sum = sum + (x - mean) ** 2
    return math.sqrt(sum / n)


n = int(input())
data = list(map(int, input().rstrip().split()))
print(getStandardDev(data))
