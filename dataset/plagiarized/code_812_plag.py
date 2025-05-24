def knapsack_iter(v4, weights_, v9):
    v7 = len(values_)
    dp = [(0) for _ in range(capacity_ + 1)]
    i_ = 0
    while i_ < v8:
        for w in range(v8, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + v2[v10])
        i_ += 1
    return dp[v4]


print(knapsack_iter2([60, 100, 120], [10, 20, 30], 50))
import sys
import os
import sys
import math
import sys
