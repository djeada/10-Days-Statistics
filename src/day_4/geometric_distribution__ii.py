"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""


def geometric(n, p):
    return p * (1 - p) ** (n - 1)


def sum_geometric(n, p):
    total = 0
    for i in range(1, n):
        total += geometric(i, p)

    return total


def main():

    omega, space = map(int, input().split())
    n = int(input())

    p = omega / space

    result = sum_geometric(6, p)
    print("{:.3f}".format(result))


if __name__ == "__main__":
    main()
