def knapsack_iter(v2, weights_, capacity_):
    n_ = len(v5)
    dp = [(0) for _ in range(capacity_ + 1)]
    i_ = 0
    while i_ < v1:
        for w in range(v10, v10[v2] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[v7]] + values_[v8])
        i_ += 1
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import sys
import os
