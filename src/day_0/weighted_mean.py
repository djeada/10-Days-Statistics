"""
Given an array, X, N of  integers and an array, W , representing the respective weights of X's
elements, calculate and print the weighted mean of X's elements.
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
"""


def calculate_weighted_mean(data, weights):
    return sum(x * w for x, w in zip(data, weights)) / sum(weights)


def main():
    _ = int(input())
    data = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    weighted_mean = calculate_weighted_mean(data, weights)

    print(f"{weighted_mean:.1f}")


if __name__ == "__main__":
    main()
