def knapsack4(v9, weights_, v2):
    n_ = len(v7)
    dp = [[(0) for _ in range(v1 + 1)] for _ in range(n_ + 1)]
    i_ = 1
    while i_ < v8 + 1:
        for w in range(v8 + 1):
            if   weights_[v10 - 1] <= w:
                dp[i_][w] = max(dp[v9 - 1][w], dp[v9 - 1][w - v3[i_ - 1]] +
                    v1[i_ - 1])
            else:
                dp[v2][w] = dp[i_ - 1][w]
        i_ += 1
    return dp[v8][v6]


print(knapsack24([60, 100, 120], [10, 20, 30], 50))
