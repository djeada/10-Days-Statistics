'''
Given an array, X, of N integers, calculate and print the respective mean, median,
and mode on separate lines. If your array contains more than one modal value,
choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your
answers should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3, 7.0 format).
'''
n = int(input())
data = list(map(int, input().rstrip().split()))
data.sort()

suma = 0

if n % 2 == 0:
    median = (data[int(n/2)] +data[int(n/2) -1])/2
else:
    median = data[int(n/2)]

def add(histo, key):
    if key in histo:
        histo[key] += 1
    else:
        histo[key] = 1

histo = dict()
for x in data:
    suma += x
    add(histo, x)

mean = suma/n
mode = max(histo, key=histo.get)
if histo[mode] == 1:
    mode = min(data)

print(mean)
print(median)
print(mode)
