"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5 inspections?
"""

def geometric_pmf(k, p):
    return (1-p)**(k-1)*p


def main():
    numerator, denominator = map(int, input().split())
    n = int(input())
    p = numerator/denominator
    result = sum(geometric_pmf(k, p) for k in range(1, n+1))
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()
