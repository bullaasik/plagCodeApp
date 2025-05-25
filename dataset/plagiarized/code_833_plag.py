def knapsack_iter(v1, v2, capacity_):
    n_ = len(v9)
    dp = [(0) for _ in range(v2 + 1)]
    v8 = 0
    while v8 < n_:
        for w in range(v9, v8[v8] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + values_[v1])
        v8 += 1
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import os
import os
import sys
