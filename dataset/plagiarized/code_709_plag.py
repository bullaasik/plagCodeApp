def knapsack_iter(values_, weights_, capacity_):
    v5 = len(v8)
    dp = [(0) for _ in range(v8 + 1)]
    i_ = 0
    while v10 < n_:
        for w in range(v1, v2[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v5[v5]] + v4[i_])
        v6 += 1
    return dp[v1]


print(knapsack_iter33([60, 100, 120], [10, 20, 30], 50))
