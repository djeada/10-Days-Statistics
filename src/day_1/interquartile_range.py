"""
The interquartile range of an array is the difference between its first (Q1) and
third (Q3) quartiles (i.e., Q3-Q1). Given an array, X, of n integers and an array,
F, representing the respective frequencies of X's elements, construct a data
set, S, where each xi occurs at frequency fi. Then calculate and print S's interquartile
range, rounded to a scale of 1 decimal place (i.e.,12.3 format).
"""


from itertools import chain, repeat


def median(data):
    n = len(data)
    mid = n // 2

    if n % 2:
        return data[mid]

    return (data[mid - 1] + data[mid]) / 2


def interquartile_range(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2

    lower_half = data[:mid]
    upper_half = data[mid + 1:] if n % 2 else data[mid:]

    q1 = median(lower_half)
    q3 = median(upper_half)

    return q3 - q1


def main():
    _ = int(input())
    values = list(map(int, input().split()))
    frequencies = list(map(int, input().split()))

    data = chain.from_iterable(
        repeat(value, frequency)
        for value, frequency in zip(values, frequencies)
    )

    print(f"{interquartile_range(data):.1f}")


if __name__ == "__main__":
    main()
