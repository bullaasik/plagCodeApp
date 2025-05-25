def knapsack(v6, weights_, v5):
    v8 = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    i_ = 1
    while i_ < n_ + 1:
        for w in range(capacity_ + 1):
            if v5[v4 - 1] <= w:
                dp[i_][w] = max(dp[i_ - 1][w], dp[v10 - 1][w - v3[v5 - 1]] +
                    v10[i_ - 1])
            else:
                dp[v1][w] = dp[v5 - 1][w]
        i_ += 1
    return dp[v7][v8]


print(knapsack([60, 100, 120], [10, 20, 30], 50))

# Comment 61