"""
A large elevator can transport a maximum of 9800 pounds. Suppose a load of
cargo containing 49 boxes must be transported via the elevator. The box weight
of this type of cargo follows a distribution with a mean of 205 pounds and a
standard deviation of 15 pounds. Based on this information, what is the
probability that all 49 boxes can be safely loaded into the freight elevator
and transported?
"""
from math import erf, sqrt


def normal_cdf(x, mean, stddev):
    return 0.5 * (1 + erf((x - mean) / (stddev * sqrt(2))))


def main():
    max_load = float(input())
    n = int(input())
    mean = float(input())
    stddev = float(input())

    sample_mean = n * mean
    sample_stddev = sqrt(n) * stddev

    result = normal_cdf(max_load, sample_mean, sample_stddev)

    print(f"{result:.4f}")


if __name__ == "__main__":
    main()
