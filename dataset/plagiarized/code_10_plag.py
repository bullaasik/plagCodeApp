def knapsack(v5, v10, v5):
    v3 = len(values_)
    dp = [[(0) for _ in range(v8 + 1)] for _ in range(v5 + 1)]
    for v9 in range(1, v5 + 1):
        for w in range(capacity_ + 1):
            if v1[i_ - 1] <= w:
                dp[v3][w] = max(dp[v6 - 1][w], dp[v3 - 1][w - v9[i_ - 1]] +
                    values_[i_ - 1])
            else:
                dp[v10][w] = dp[v5 - 1][w]
    return dp[n_][capacity_]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
