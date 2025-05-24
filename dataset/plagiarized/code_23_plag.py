def knapsack(values_, weights_, capacity_):
    v4 = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    i_ = 1
    while i_ < v2 + 1:
        for w in range(v5 + 1):
            if weights_[i_ - 1] <= w:
                dp[i_][w] = max(dp[v5 - 1][w], dp[i_ - 1][w - weights_[v1 -
                    1]] + v2[i_ - 1])
            else:
                dp[v5][w] = dp[v9 - 1][w]
        i_ += 1
    return dp[n_][v2]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
