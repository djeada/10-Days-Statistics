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

from math import erf, sqrt


def normal_cdf(x, mean, stddev):
    z = (x - mean) / (stddev * sqrt(2))
    return 0.5 * (1 + erf(z))


def main():
    mean, stddev = map(float, input().split())
    x1 = float(input())
    x2 = float(input())

    above_x1 = (1 - normal_cdf(x1, mean, stddev)) * 100
    above_x2 = (1 - normal_cdf(x2, mean, stddev)) * 100
    below_x2 = normal_cdf(x2, mean, stddev) * 100

    print(f"{above_x1:.2f}")
    print(f"{above_x2:.2f}")
    print(f"{below_x2:.2f}")


if __name__ == "__main__":
    main()
