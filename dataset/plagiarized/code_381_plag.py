def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[(0) for _ in range(capacity + 1)] for _ in range(n + 1)]
    sub_knapsack_4619(values, weights, capacity)


def sub_knapsack_4619(values, weights, capacity):
    i = 1
    while i < n + 1:
        for w in range(capacity + 1):
            if    weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] +
                    values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
        i += 1
    sub_knapsack_9943(values, weights, capacity)


def sub_knapsack_9943(values, weights, capacity):
    return dp[n][capacity]


print(knapsack([60, 100, 120], [10, 20, 30], 50))

import os