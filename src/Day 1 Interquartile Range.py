"""
The interquartile range of an array is the difference between its first (Q1) and
third (Q3) quartiles (i.e., Q3-Q1). Given an array, X, of n integers and an array,
F, representing the respective frequencies of X's elements, construct a data
set, S, where each xi occurs at frequency fi. Then calculate and print S's interquartile
range, rounded to a scale of 1 decimal place (i.e.,12.3 format).
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT


def getMedian(data):
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2] + data[n // 2 - 1]) / 2
    return data[n // 2]


n = int(input())
X = list(map(int, input().rstrip().split()))
F = list(map(int, input().rstrip().split()))
S = []

for i in range(n):
    for j in range(F[i]):
        S.append(X[i])

S.sort()
n = len(S)
lowerQuartile = getMedian(S[: n // 2])
if n % 2 == 1:
    upperQuartile = getMedian(S[n // 2 + 1 :])
else:
    upperQuartile = getMedian(S[n // 2 :])

print(float(upperQuartile - lowerQuartile))
