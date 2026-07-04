"""
In a certain plant, the time taken to assemble a car is a random variable,X ,
having a normal distribution with a mean of 20 hours and a standard deviation of
2 hours. What is the probability that a car can be assembled at this plant in:
Less than 19.5 hours?
Between 20 and 22 hours?
"""

from math import erf, sqrt


def normal_cdf(x, mean, stddev):
    return 0.5 * (1 + erf((x - mean) / (stddev * sqrt(2))))


def main():
    mean, stddev = map(float, input().split())
    x = float(input())
    lower, upper = map(float, input().split())

    less_than_x = normal_cdf(x, mean, stddev)
    between_lower_and_upper = normal_cdf(upper, mean, stddev) - normal_cdf(
        lower,
        mean,
        stddev,
    )

    print(f"{less_than_x:.3f}")
    print(f"{between_lower_and_upper:.3f}")


if __name__ == "__main__":
    main()
