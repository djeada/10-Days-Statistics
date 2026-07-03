"""
Given an array, X, of n integers, calculate the respective first quartile (Q1),
second quartile (Q2), and third quartile (Q3).
It is guaranteed that Q1, Q2, and Q3 are integers.
"""


def median(data):
    n = len(data)
    mid = n // 2

    if n % 2:
        return data[mid]

    return (data[mid - 1] + data[mid]) / 2


def quartiles(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2

    lower_half = data[:mid]
    upper_half = data[mid + 1:] if n % 2 else data[mid:]

    q1 = median(lower_half)
    q2 = median(data)
    q3 = median(upper_half)

    return q1, q2, q3


def main():
    _ = int(input())
    data = list(map(int, input().split()))

    for q in quartiles(data):
        print(int(q))


if __name__ == "__main__":
    main()
