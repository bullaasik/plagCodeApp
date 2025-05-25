def knapsack(v1, v6, v9):
    n_ = len(v8)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v1 + 1)]
    v4 = 1
    while v4 < v5 + 1:
        w = 0
        while w < capacity_ + 1:
            if weights_[v9 - 1] <= w:
                dp[v3][w] = max(dp[v1 - 1][w], dp[v5 - 1][w - v1[v7 - 1]] +
                    v6[i_ - 1])
            else:
                dp[i_][w] = dp[v6 - 1][w]
            w += 1
        v4 += 1
    return dp[n_][v2]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
