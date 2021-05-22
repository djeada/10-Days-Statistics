"""
Given an array, X, N of  integers and an array, W , representing the respective weights of X's
elements, calculate and print the weighted mean of X's elements.
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
"""
n = int(input())
data = list(map(int, input().rstrip().split()))
weighs = list(map(int, input().rstrip().split()))

m = 0
suma = 0

for i in range(n):
    m += data[i] * weighs[i]
    suma += weighs[i]
m /= suma

print("{:.1f}".format(m))
