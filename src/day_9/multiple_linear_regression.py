"""
Andrea has a simple equation:
Y = a + b1f1 + b2f2 + ... + bmfm
for (m + 1) real constants (a, f1, f2, ..., fm). We can say that the value of Y depends on m features. 
Andrea studies this equation for n different feature sets (f1, f2, ..., fm) and records each respective value of Y. 
If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?
"""

def solve_linear_system(matrix, values):
    n = len(values)
    augmented = [row[:] + [value] for row, value in zip(matrix, values)]

    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(augmented[row][col]))
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]

        pivot_value = augmented[col][col]
        augmented[col] = [value / pivot_value for value in augmented[col]]

        for row in range(n):
            if row == col:
                continue

            factor = augmented[row][col]
            augmented[row] = [
                current - factor * pivot_current
                for current, pivot_current in zip(augmented[row], augmented[col])
            ]

    return [row[-1] for row in augmented]


def least_squares(samples, feature_count):
    x = [[1.0] + sample[:feature_count] for sample in samples]
    y = [sample[-1] for sample in samples]

    columns = list(zip(*x))

    left = [
        [
            sum(a * b for a, b in zip(col_a, col_b))
            for col_b in columns
        ]
        for col_a in columns
    ]

    right = [
        sum(value * target for value, target in zip(col, y))
        for col in columns
    ]

    return solve_linear_system(left, right)


def predict(coefficients, features):
    intercept, *weights = coefficients
    return intercept + sum(weight * value for weight, value in zip(weights, features))


def main():
    feature_count, sample_count = map(int, input().split())

    samples = [
        list(map(float, input().split()))
        for _ in range(sample_count)
    ]

    coefficients = least_squares(samples, feature_count)

    query_count = int(input())

    for _ in range(query_count):
        features = list(map(float, input().split()))
        print(f"{predict(coefficients, features):.3f}")


if __name__ == "__main__":
    main()
