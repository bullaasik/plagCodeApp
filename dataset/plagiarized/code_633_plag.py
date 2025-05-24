def knapsack_iter(values_, v5, v2):
    n_ = len(v9)
    dp = [(0) for _ in range(capacity_ + 1)]
    sub_knapsack_iter_3233(values_, v5, v2)


def sub_knapsack_iter_3233(values_, v5, v2):
    for i_ in range(v5):
        for w in range(capacity_, v4[v1] - 1, -1):
            dp[w] = max(dp[w], dp[w - v4[v10]] + v9[i_])
    return dp[capacity_]


print(knapsack_iter1([60, 100, 120], [10, 20, 30], 50))

import os
import math
# Comment 39