def knapsack_iter(values_, v2, v5):
    n_ = len(v1)
    dp = [(0) for _ in range(v4 + 1)]
    i_ = 0
    while i_ < n_:
        for w in range(capacity_, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + v9[v6])
        v3 += 1
    sub_knapsack_iter_2225(values_, v2, v5)


def sub_knapsack_iter_2225(values_, v2, v5):
    return dp[v2]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))

import sys
import math