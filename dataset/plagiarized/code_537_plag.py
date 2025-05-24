def knapsack_iter(v2, v3, capacity_):
    v4 = len(v5)
    dp = [(0) for _ in range(v4 + 1)]
    v2 = 0
    while v2 < v4:
        for w in range(v8, weights_[v8] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[v7]] + v2[v6])
        v2 += 1
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
