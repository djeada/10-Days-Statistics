"""
Given an array, X, of N integers, calculate and print the respective mean, median,
and mode on separate lines. If your array contains more than one modal value,
choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your
answers should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3, 7.0 format).
"""

from collections import Counter


def mean(data):
    return sum(data) / len(data)


def median(data):
    n = len(data)
    mid = n // 2

    if n % 2:
        return data[mid]

    return (data[mid - 1] + data[mid]) / 2


def mode(data):
    counts = Counter(data)
    max_count = max(counts.values())

    return min(value for value, count in counts.items() if count == max_count)


def main():
    _ = int(input())
    data = sorted(map(int, input().split()))

    print(f"{mean(data):.1f}")
    print(f"{median(data):.1f}")
    print(mode(data))


if __name__ == "__main__":
    main()
