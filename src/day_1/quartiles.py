"""
Given an array, X, of n integers, calculate the respective first quartile (Q1),
second quartile (Q2), and third quartile (Q3).
It is guaranteed that Q1, Q2, and Q3 are integers.
"""


def getMedian(data):
    n = len(data)
    if n % 2 == 0:
        return int((data[int(n / 2)] + data[int(n / 2) - 1]) / 2)
    return data[int(n / 2)]


n = int(input())
data = list(map(int, input().rstrip().split()))
data.sort()

median = getMedian(data)
lowerQuartile = getMedian(data[: int(n / 2)])

if n % 2 == 1:
    upperQuartile = getMedian(data[int(n / 2) + 1 :])
else:
    upperQuartile = getMedian(data[int(n / 2) :])

print(lowerQuartile)
print(median)
print(upperQuartile)
