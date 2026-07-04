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


def linear_regression(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    intercept = (sum_y / n) - slope * (sum_x / n)

    return intercept, slope


def main():
    data = [tuple(map(int, input().split())) for _ in range(5)]
    x, y = zip(*data)

    intercept, slope = linear_regression(x, y)

    prediction = intercept + slope * 80
    print(f"{prediction:.3f}")


if __name__ == "__main__":
    main()
