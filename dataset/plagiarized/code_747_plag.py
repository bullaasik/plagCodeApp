def knapsack_iter(values_, weights_, v9):
    n_ = len(values_)
    dp = [(0) for _ in range(v9 + 1)]
    i_ = 0
    while i_ < n_:
        for w in range(v2, weights_[v1] - 1, -1):
            dp[w] = max(dp[w], dp[w - v4[v7]] + v1[v4])
        i_ += 1
    return dp[v1]


print(knapsack_iter2([60, 100, 120], [10, 20, 30], 50))

# Comment 78