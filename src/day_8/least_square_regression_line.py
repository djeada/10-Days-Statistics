"""
A group of five students enrolls in Statistics immediately after
taking a Math aptitude test. Each student's Math aptitude test score, x,
and Statistics course grade, y , can be expressed as the following list
of  points.
If a student scored an 80 on the Math aptitude test, what grade would
we expect them to achieve in Statistics? Determine the equation of the
best-fit line using the least squares method, then compute and print the
value of y when x = 80.
"""


def linearRegression(X, Y, n):
    sumX = 0
    for i in range(n):
        sumX += X[i]
    sumXsq = 0
    for i in range(n):
        sumXsq += X[i] ** 2
    sumY = 0
    for i in range(n):
        sumY += Y[i]
    sumXY = 0
    for i in range(n):
        sumXY += X[i] * Y[i]

    b = (n * sumXY - sumX * sumY) / (n * sumXsq - sumX ** 2)
    a = mean(Y) - b * mean(X)
    return a, b


def mean(tab):
    return sum(tab) / len(tab)


X, Y = [0] * 5, [0] * 5
for i in range(5):
    X[i], Y[i] = map(int, input().split())

a, b = linearRegression(X, Y, 5)

print("{:.3f}".format(a + b * 80))
