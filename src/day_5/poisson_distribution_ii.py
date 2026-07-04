"""
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating  is 160 + 40*X^2.
The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating  is 120 + 40*Y^2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""

def expected_value_squared(lam):
    return lam + lam**2


def main():
    lambda_a, lambda_b = map(float, input().split())

    cost_a = 160 + 40 * expected_value_squared(lambda_a)
    cost_b = 128 + 40 * expected_value_squared(lambda_b)

    print(f"{cost_a:.3f}")
    print(f"{cost_b:.3f}")


if __name__ == "__main__":
    main()
