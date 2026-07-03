"""
Given an array, X, of N integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the
standard deviation.
"""

from math import sqrt


def mean(data):
    return sum(data) / len(data)


def standard_deviation(data):
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)

    return sqrt(variance)


def main():
    _ = int(input())
    data = list(map(int, input().split()))

    print(f"{standard_deviation(data):.1f}")


if __name__ == "__main__":
    main()
