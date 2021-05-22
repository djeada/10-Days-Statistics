"""
Given two n-element data sets, X and Y, calculate the value
of  Spearman's rank correlation coefficient.
"""


def spearman(n, X, Y):
    rankX = rank(n, X)
    rankY = rank(n, Y)

    r = 0
    for i in range(n):
        r += (rankX[i] - rankY[i]) ** 2

    return 1 - 6 * r / (n * (n ** 2 - 1))


def rank(n, X):
    r = [0] * len(X)
    temp1 = sorted(X)
    temp2 = dict()
    x = 1
    temp2[temp1[0]] = 1
    for i in range(1, n):
        if temp1[i] != temp1[i - 1]:
            x += 1
        temp2[temp1[i]] = x
    for i in range(n):
        r[i] = temp2[X[i]]

    return r


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print("{:.3f}".format(spearman(n, X, Y)))
