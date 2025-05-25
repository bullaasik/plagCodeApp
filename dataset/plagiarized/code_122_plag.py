def knapsack5(v7, weights_, v3):
    n_ = len(v9)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v2 + 1)]
    v2 = 1
    while v1 < v3 + 1:
        w = 0
        while w < capacity_ + 1:
            if weights_[v2 - 1] <= w:
                dp[v2][w] = max(dp[v8 - 1][w], dp[i_ - 1][w - v2[v8 - 1]] +
                    values_[i_ - 1])
            else:
                dp[i_][w] = dp[v7 - 1][w]
            w += 1
        v6 += 1
    return dp[n_][capacity_]


print(knapsack2([60, 100, 120], [10, 20, 30], 50))
