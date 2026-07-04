"""
The number of tickets purchased by each student for the University X vs.
University Y football game follows a distribution that has a mean of 2.4
and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase
last-minute tickets. If there are only 250 tickets left, what is the probability
that all 100 students will be able to purchase tickets?
"""
from math import erf, sqrt


def normal_cdf(x, mean, stddev):
    return 0.5 * (1 + erf((x - mean) / (stddev * sqrt(2))))


def main():
    tickets = float(input())
    students = int(input())
    mean = float(input())
    stddev = float(input())

    total_mean = students * mean
    total_stddev = sqrt(students) * stddev

    result = normal_cdf(tickets, total_mean, total_stddev)

    print(f"{result:.4f}")


if __name__ == "__main__":
    main()
