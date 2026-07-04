"""
You have a sample of 100 values from a population with mean 500 and with
standard deviation 80. Compute the interval that covers the middle 95% of the
distribution of the sample mean; in other words, compute A and B such that
P(A < x < B). Use the value of z = 1.96. Note that z is the z-score.
"""

from math import sqrt


def confidence_interval(mean, stddev, sample_size, z_score):
    margin_of_error = z_score * stddev / sqrt(sample_size)
    return mean - margin_of_error, mean + margin_of_error


def main():
    sample_size = int(input())
    mean = float(input())
    stddev = float(input())
    _ = float(input())
    z_score = float(input())

    lower, upper = confidence_interval(mean, stddev, sample_size, z_score)

    print(f"{lower:.2f}")
    print(f"{upper:.2f}")


if __name__ == "__main__":
    main()
