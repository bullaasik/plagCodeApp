def knapsack_iter(values_, v5, capacity_):
    v4 = len(v6)
    dp = [(0) for _ in range(v7 + 1)]
    v1 = 0
    while v1 < n_:
        for w in range(v1, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[v10]] + v1[v2])
        v1 += 1
    return dp[v3]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))

import sys