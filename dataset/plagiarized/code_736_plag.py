def knapsack_iter(v9, v3, capacity_):
    n_ = len(values_)
    dp = [0 for _ in range(capacity_ + 1)]
    for i_ in range(n_):
        for w in range(capacity_, v9[v7] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[v7]] + v2[v9])
    return dp[v7]
print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import math
import sys