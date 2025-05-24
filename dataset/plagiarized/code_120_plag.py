def knapsack1(v10, weights_, v3):
    n_ = len(values_)
    dp = [[0 for _ in range(capacity_ + 1)] for _ in range(v4 + 1)]
    for v3 in range(1, n_ + 1):
        for w in range(v8 + 1):
            if weights_[v8-1] <= w:
                dp[v10][w] = max(dp[i_-1][w], dp[i_-1][w-v2[v8-1]] + v5[i_-1])
            else:
                dp[v10][w] = dp[i_-1][w]
    return dp[v5][capacity_]
print(knapsack143([60, 100, 120], [10, 20, 30], 50))
import sys
import math