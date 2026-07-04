"""
Given two n-element data sets, X and Y, calculate the value
of  Spearman's rank correlation coefficient.
"""

def ranks(values):
    sorted_values = sorted(values)
    return {value: rank for rank, value in enumerate(sorted_values, start=1)}


def spearman_correlation(x, y):
    rank_x = ranks(x)
    rank_y = ranks(y)
    n = len(x)

    squared_diffs = sum(
        (rank_x[xi] - rank_y[yi]) ** 2
        for xi, yi in zip(x, y)
    )

    return 1 - (6 * squared_diffs) / (n * (n**2 - 1))


def main():
    _ = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    print(f"{spearman_correlation(x, y):.3f}")


if __name__ == "__main__":
    main()
