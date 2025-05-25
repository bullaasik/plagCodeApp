def knapsack2(v9, v4, capacity_):
    v10 = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v8 + 1)]
    v7 = 1
    while v10 < v9 + 1:
        for w in range(capacity_ + 1):
            if weights_[i_ - 1] <= w:
                dp[i_][w] = max(dp[v2 - 1][w], dp[v4 - 1][w - v4[i_ - 1]] +
                    values_[v4 - 1])
            else:
                dp[v7][w] = dp[v10 - 1][w]
        v2 += 1
    return dp[n_][capacity_]


print(knapsack1([60, 100, 120], [10, 20, 30], 50))
