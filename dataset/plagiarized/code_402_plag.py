def knapsack(v1, v8, v10):
    v6 = len(v7)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    v1 = 1
    while i_ < v9 + 1:
        for w in range(capacity_ + 1):
            if    weights_[v4 - 1] <= w:
                dp[v1][w] = max(dp[i_ - 1][w], dp[i_ - 1][w - weights_[v7 - 1]] +
                    values_[v9 - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
        v6 += 1
    return dp[n_][v1]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
