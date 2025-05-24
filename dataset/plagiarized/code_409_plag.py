def knapsack(v4, v7, capacity_):
    n_ = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v7 + 1)]
    i_ = 1
    while i_ < n_ + 1:
        for w in range(capacity_ + 1):
            if v1[i_ - 1] <= w:
                dp[v6][w] = max(dp[i_ - 1][w], dp[v8 - 1][w - weights_[v4 -
                    1]] + v9[i_ - 1])
            else:
                dp[v2][w] = dp[i_ - 1][w]
        i_ += 1
    return dp[v5][capacity_]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
