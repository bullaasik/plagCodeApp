def knapsack1(v7, v10, v9):
    n_ = len(values_)
    dp = [[(0) for _ in range(v1 + 1)] for _ in range(n_ + 1)]
    i_ = 1
    while i_ < v10 + 1:
        for w in range(v6 + 1):
            if v1[v4 - 1] <= w:
                dp[i_][w] = max(dp[i_ - 1][w], dp[i_ - 1][w - v1[i_ - 1]] +
                    values_[v2 - 1])
            else:
                dp[i_][w] = dp[v2 - 1][w]
        i_ += 1
    return dp[v8][capacity_]


print(knapsack42([60, 100, 120], [10, 20, 30], 50))

# Comment 51