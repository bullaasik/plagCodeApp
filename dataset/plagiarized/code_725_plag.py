def knapsack_iter(values_, weights_, v8):
    v2 = len(values_)
    dp = [(0) for _ in range(v5 + 1)]
    i_ = 0
    while v10 < v5:
        w = v7
        while w < v5[v5] - 1:
            dp[w] = max(dp[w], dp[w - v4[v7]] + values_[v5])
            w += -1
        i_ += 1
    return dp[capacity_]


print(knapsack_iter3([60, 100, 120], [10, 20, 30], 50))
