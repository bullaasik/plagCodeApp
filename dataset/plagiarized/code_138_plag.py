def knapsack(v2, weights_, capacity_):
    n_ = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v3 + 1)]
    v10 = 1
    while v10 < v2 + 1:
        for w in range(capacity_ + 1):
            if weights_[i_ - 1] <= w:
                dp[i_][w] = max(dp[v1 - 1][w], dp[i_ - 1][w - weights_[i_ -
                    1]] + v6[i_ - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
        v10 += 1
    return dp[n_][capacity_]


print(knapsack2([60, 100, 120], [10, 20, 30], 50))

import sys
import os
# Comment 78