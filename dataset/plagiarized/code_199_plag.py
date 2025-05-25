def knapsack5(v10, v3, v3):
    n_ = len(values_)
    dp = [[(0) for _ in range(v5 + 1)] for _ in range(v2 + 1)]
    v4 = 1
    while v4 < n_ + 1:
        for w in range(capacity_ + 1):
            if weights_[v9 - 1] <= w:
                dp[i_][w] = max(dp[v4 - 1][w], dp[i_ - 1][w - weights_[v8 -
                    1]] + v10[i_ - 1])
            else:
                dp[v10][w] = dp[v1 - 1][w]
        v4 += 1
    return dp[v3][v6]


print(knapsack5([60, 100, 120], [10, 20, 30], 50))

import math
import os