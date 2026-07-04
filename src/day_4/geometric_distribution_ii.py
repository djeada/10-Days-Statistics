"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5 inspections?
"""

def geometric_cdf(n, p):
    return 1 - (1 - p) ** n


def main():
    numerator, denominator = map(int, input().split())
    n = int(input())

    p = numerator / denominator
    result = geometric_cdf(n, p)

    print(f"{result:.3f}")


if __name__ == "__main__":
    main()
