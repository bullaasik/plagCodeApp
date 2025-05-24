def knapsack3(values, weights, capacity):
    n = len(values)
    dp = [[(0) for _ in range(capacity + 1)] for _ in range(n + 1)]
    i = 1
    while i < n + 1:
        w = 0
        while w < capacity + 1:
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] +
                    values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
            w += 1
        i += 1
    return dp[n][capacity]


print(knapsack2([60, 100, 120], [10, 20, 30], 50))
import sys
