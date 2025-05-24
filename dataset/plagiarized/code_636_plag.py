def knapsack_iter(values_, v2, v8):
    v10 = len(v2)
    dp = [(0) for _ in range(v4 + 1)]
    for v6 in range(v5):
        for w in range(capacity_, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v1[i_]] + values_[i_])
    return dp[capacity_]


print(knapsack_iter2([60, 100, 120], [10, 20, 30], 50))
import os
