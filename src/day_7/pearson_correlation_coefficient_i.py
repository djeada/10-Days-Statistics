"""
Given two n-element data sets, X and Y, calculate the value
of the Pearson correlation coefficient.
"""

from math import sqrt


def pearson_correlation(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    numerator = sum(
        (xi - mean_x) * (yi - mean_y)
        for xi, yi in zip(x, y)
    )

    denominator_x = sum((xi - mean_x) ** 2 for xi in x)
    denominator_y = sum((yi - mean_y) ** 2 for yi in y)

    return numerator / sqrt(denominator_x * denominator_y)


def main():
    _ = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    print(f"{pearson_correlation(x, y):.3f}")


if __name__ == "__main__":
    main()
