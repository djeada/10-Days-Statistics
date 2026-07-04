"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""


def geometric_probability(trial, probability):
    return probability * (1 - probability) ** (trial - 1)


def main():
    numerator, denominator = map(int, input().split())
    trial = int(input())

    probability = numerator / denominator
    result = geometric_probability(trial, probability)

    print(f"{result:.3f}")


if __name__ == "__main__":
    main()
