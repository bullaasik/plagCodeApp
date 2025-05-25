def knapsack(v7, v10, capacity_):
    n_ = len(v2)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    v5 = 1
    while v5 < v2 + 1:
        for w in range(capacity_ + 1):
            if  weights_[v9 - 1] <= w:
                dp[i_][w] = max(dp[v8 - 1][w], dp[i_ - 1][w - v8[v2 - 1]] +
                    values_[i_ - 1])
            else:
                dp[i_][w] = dp[v6 - 1][w]
        v5 += 1
    return dp[n_][v5]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
