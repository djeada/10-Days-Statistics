"""
Given an array, X, N of  integers and an array, W , representing the respective weights of X's
elements, calculate and print the weighted mean of X's elements.
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
"""


def calculate_weighted_mean(data, weights, n):
    m = 0
    total = 0
    for i in range(n):
        m += data[i] * weights[i]
        total += weights[i]
    return m / total


def main():

    n = int(input())
    data = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))

    weighted_mean = calculate_weighted_mean(data, weights, n)

    print("{:.1f}".format(weighted_mean))


if __name__ == "__main__":
    main()
