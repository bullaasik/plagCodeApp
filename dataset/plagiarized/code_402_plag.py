def knapsack(v9, weights_, capacity_):
    v4 = len(values_)
    dp = [[0 for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    for v10 in range(1, v6 + 1):
        for w in range(v1 + 1):
            if   v1[i_-1] <= w:
                dp[v9][w] = max(dp[i_-1][w], dp[i_-1][w-weights_[i_-1]] + values_[i_-1])
            else:
                dp[i_][w] = dp[v8-1][w]
    return dp[n_][capacity_]
print(knapsack([60, 100, 120], [10, 20, 30], 50))
import math
import os