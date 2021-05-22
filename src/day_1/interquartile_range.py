"""
The interquartile range of an array is the difference between its first (Q1) and
third (Q3) quartiles (i.e., Q3-Q1). Given an array, X, of n integers and an array,
F, representing the respective frequencies of X's elements, construct a data
set, S, where each xi occurs at frequency fi. Then calculate and print S's interquartile
range, rounded to a scale of 1 decimal place (i.e.,12.3 format).
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


def calculate_inter_quartile(S, n):
    lower_quartile = calculate_lower_quartile(S, n)
    upper_quartile = calculate_upper_quartile(S, n)

    return float(upper_quartile - lower_quartile)


def main():

    n = int(input())
    X = list(map(int, input().rstrip().split()))
    F = list(map(int, input().rstrip().split()))
    S = []

    for i in range(n):
        for j in range(F[i]):
            S.append(X[i])

    S.sort()
    n = len(S)

    print(calculate_inter_quartile(S, n))


if __name__ == "__main__":
    main()
