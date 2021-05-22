"""
Given an array, X, of n integers, calculate the respective first quartile (Q1),
second quartile (Q2), and third quartile (Q3).
It is guaranteed that Q1, Q2, and Q3 are integers.
"""


def calculate_median(data):
    n = len(data)

    if n % 2 == 0:
        return (data[n // 2] + data[n // 2 - 1]) / 2

    return data[n // 2]


def calculate_lower_quartile(S, n):
    return calculate_median(S[: n // 2])


def calculate_upper_quartile(S, n):

    if n % 2 == 1:
        return calculate_median(S[n // 2 + 1 :])

    return calculate_median(S[n // 2 :])


def main():

    n = int(input())
    data = list(map(int, input().rstrip().split()))
    data.sort()

    median = calculate_median(data)
    lower_quartile = calculate_lower_quartile(data, n)
    upper_quartile = calculate_upper_quartile(data, n)

    print(int(lower_quartile))
    print(int(median))
    print(int(upper_quartile))


if __name__ == "__main__":
    main()
