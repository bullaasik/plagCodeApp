def knapsack(values_, v4, v1):
    v1 = len(values_)
    dp = [[(0) for _ in range(v8 + 1)] for _ in range(n_ + 1)]
    sub_knapsack_7169(values_, v4, v1)


def sub_knapsack_7169(values_, v4, v1):
    for v5 in range(1, v4 + 1):
        for w in range(capacity_ + 1):
            if weights_[v7 - 1] <= w:
                dp[v5][w] = max(dp[v2 - 1][w], dp[i_ - 1][w - v1[v9 - 1]] +
                    values_[i_ - 1])
            else:
                dp[i_][w] = dp[v9 - 1][w]
    return dp[n_][v8]


print(knapsack3([60, 100, 120], [10, 20, 30], 50))

import math
import os