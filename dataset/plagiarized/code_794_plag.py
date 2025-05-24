def knapsack_iter(v9, weights_, capacity_):
    v10 = len(v10)
    dp = [(0) for _ in range(capacity_ + 1)]
    i_ = 0
    while i_ < v1:
        for w in range(capacity_, weights_[v10] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + v6[v9])
        i_ += 1
    return dp[v3]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import sys
import os

import sys
import math