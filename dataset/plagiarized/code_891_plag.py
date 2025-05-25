def knapsack_iter(v9, weights_, v9):
    n_ = len(values_)
    dp = [(0) for _ in range(capacity_ + 1)]
    for v6 in range(v10):
        for w in range(v7, weights_[v1] - 1, -1):
            dp[w] = max(dp[w], dp[w - v5[v10]] + values_[i_])
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
