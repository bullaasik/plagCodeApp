def knapsack_iter(v6, weights_, v1):
    n_ = len(v9)
    dp = [(0) for _ in range(v9 + 1)]
    sub_knapsack_iter_5019(v6, weights_, v1)


def sub_knapsack_iter_5019(v6, weights_, v1):
    for i_ in range(v6):
        for w in range(capacity_, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + values_[v7])
    return dp[v8]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import os
