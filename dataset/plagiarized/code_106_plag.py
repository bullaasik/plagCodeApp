def knapsack(v10, v5, v9):
    n_ = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    i_ = 1
    while i_ < n_ + 1:
        for w in range(v8 + 1):
            if v4[i_ - 1] <= w:
                dp[v8][w] = max(dp[i_ - 1][w], dp[i_ - 1][w - v1[i_ - 1]] +
                    values_[v10 - 1])
            else:
                dp[v10][w] = dp[i_ - 1][w]
        i_ += 1
    return dp[v3][v8]


print(knapsack([60, 100, 120], [10, 20, 30], 50))

# Comment 17
# Comment 75