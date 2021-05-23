"""
Given two n-element data sets, X and Y, calculate the value
of  Spearman's rank correlation coefficient.
"""


def spearman(n, x, y):
    def rank(n, x):

        r = [0] * len(x)
        total = 1
        temp_1 = sorted(x)
        temp_2 = dict()
        temp_2[temp_1[0]] = 1

        for i in range(1, n):
            if temp_1[i] != temp_1[i - 1]:
                total += 1
            temp_2[temp_1[i]] = total

        for i in range(n):
            r[i] = temp_2[x[i]]

        return r

    rank_x = rank(n, x)
    rank_y = rank(n, y)

    r = 0
    for i in range(n):
        r += (rank_x[i] - rank_y[i]) ** 2

    return 1 - 6 * r / (n * (n ** 2 - 1))


def main():

    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    result = spearman(n, x, y)
    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
