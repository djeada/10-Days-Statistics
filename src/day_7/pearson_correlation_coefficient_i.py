"""
Given two n-element data sets, X and Y, calculate the value
of the Pearson correlation coefficient.
"""


def pearson(n, x, y):
    sx = 0
    sy = 0
    p = 0

    mx = sum(x) / n
    my = sum(y) / n

    for i in range(n):
        sx += (x[i] - mx) ** 2
        sy += (y[i] - my) ** 2
        p += (x[i] - mx) * (y[i] - my)

    sx = (sx / n) ** 0.5
    sy = (sy / n) ** 0.5

    return p / (n * sx * sy)


def main():

    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    result = pearson(n, x, y)
    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
