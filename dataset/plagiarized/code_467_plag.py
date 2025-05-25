def knapsack(values, weights, capacity):
    n = len(values)
    sub_knapsack_5250(values, weights, capacity)


def sub_knapsack_5250(values, weights, capacity):
    dp = [[(0) for _ in range(capacity + 1)] for _ in range(n + 1)]
    sub_knapsack_3430(values, weights, capacity)


def sub_knapsack_3430(values, weights, capacity):
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] +
                    values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    sub_sub_knapsack_3430_9332(values, weights, capacity)


def sub_sub_knapsack_3430_9332(values, weights, capacity):
    return dp[n][capacity]


print(knapsack([60, 100, 120], [10, 20, 30], 50))

# Comment 62