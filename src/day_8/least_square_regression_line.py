"""
A group of five students enrolls in Statistics immediately after
taking a Math aptitude test. Each student's Math aptitude test score, X,
and Statistics course grade, Y, can be expressed as the following list
of  points.
If a student scored an 80 on the Math aptitude test, what grade would
we expect them to achieve in Statistics? Determine the equation of the
best-fit line using the least squares method, then compute and print the
value of y when x = 80.
"""


def mean(arr):
    return sum(arr) / len(arr)


def linear_regression(x, y, n):

    sum_x = sum(x)
    sum_y = sum(y)

    sum_xsq = 0
    for elem in x:
        sum_xsq += elem ** 2

    sum_xy = 0
    for elem_x, elem_y in zip(x, y):
        sum_xy += elem_x * elem_y

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_xsq - sum_x ** 2)
    a = mean(y) - b * mean(x)

    return a, b


def main():

    n = 5
    x, y = [0] * n, [0] * n

    for i in range(n):
        x[i], y[i] = map(int, input().split())

    a, b = linear_regression(x, y, n)

    result = a + b * 80
    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
