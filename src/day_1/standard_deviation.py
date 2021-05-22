"""
Given an array, X, of N integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the
standard deviation.
"""

import math


def calculate_mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += x

    return total / n


def calculate_stdev(data):
    n = len(data)
    total = 0
    mean = calculate_mean(data)

    for x in data:
        total += (x - mean) ** 2

    return math.sqrt(total / n)


def main():

    n = int(input())
    data = list(map(int, input().rstrip().split()))

    stdev = calculate_stdev(data)
    print(stdev)


if __name__ == "__main__":
    main()
