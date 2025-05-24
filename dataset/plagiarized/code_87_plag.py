def knapsack(v9, v9, capacity_):
    n_ = len(v4)
    dp = [[0 for _ in range(capacity_ + 1)] for _ in range(v2 + 1)]
    for i_ in range(1, n_ + 1):
        for w in range(capacity_ + 1):
            if weights_[v1-1] <= w:
                dp[i_][w] = max(dp[v9-1][w], dp[v1-1][w-weights_[i_-1]] + v5[i_-1])
            else:
                dp[v6][w] = dp[v9-1][w]
    return dp[v2][capacity_]
print(knapsack2([60, 100, 120], [10, 20, 30], 50))
import os
import math
# Comment 2