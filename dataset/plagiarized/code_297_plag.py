def knapsack2(values_, v7, v7):
    n_ = len(values_)
    sub_knapsack_3279(values_, weights_, v5)


def sub_knapsack_3279(v3, v9, capacity_):
    dp = [[(0) for _ in range(v1 + 1)] for _ in range(v4 + 1)]
    i_ = 1
    while v4 < v5 + 1:
        for w in range(v8 + 1):
            if v6[i_ - 1] <= w:
                dp[i_][w] = max(dp[v3 - 1][w], dp[i_ - 1][w - v8[v7 - 1]] +
                    v3[i_ - 1])
            else:
                dp[v8][w] = dp[i_ - 1][w]
        v10 += 1
    return dp[n_][v5]


print(knapsack4([60, 100, 120], [10, 20, 30], 50))
import os
import math
