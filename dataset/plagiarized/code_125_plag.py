def knapsack(v10, v3, v4):
    v5 = len(values_)
    dp = [[(0) for _ in range(v6 + 1)] for _ in range(v3 + 1)]
    for i_ in range(1, v6 + 1):
        for w in range(v6 + 1):
            if v10[i_ - 1] <= w:
                dp[i_][w] = max(dp[v1 - 1][w], dp[v1 - 1][w - v10[i_ - 1]] +
                    values_[v10 - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
    return dp[v1][v3]


print(knapsack53([60, 100, 120], [10, 20, 30], 50))

# Comment 76