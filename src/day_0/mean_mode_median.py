"""
Given an array, X, of N integers, calculate and print the respective mean, median,
and mode on separate lines. If your array contains more than one modal value,
choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your
answers should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3, 7.0 format).
"""


def calculate_median(data, n):
    if n % 2 == 0:
        return (data[int(n / 2)] + data[int(n / 2) - 1]) / 2

    return data[int(n / 2)]


def calculate_mean(data, n):
    total = 0

    for x in data:
        total += x

    return total / n


def calculate_mode(data, n):

    histo = dict()

    for x in data:
        if x in histo:
            histo[x] += 1
        else:
            histo[x] = 1

    mode = max(histo, key=histo.get)
    if histo[mode] == 1:
        mode = min(data)

    return mode


def main():

    n = int(input())
    data = list(map(int, input().rstrip().split()))
    data.sort()

    median = calculate_median(data, n)
    mean = calculate_mean(data, n)
    mode = calculate_mode(data, n)

    print(mean)
    print(median)
    print(mode)


if __name__ == "__main__":
    main()
