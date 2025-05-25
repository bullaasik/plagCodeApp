def knapsack_iter(v3, v2, capacity_):
    n_ = len(v6)
    dp = [(0) for _ in range(capacity_ + 1)]
    v5 = 0
    while v5 < n_:
        for w in range(capacity_, v8[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v4[i_]] + v6[i_])
        v5 += 1
    return dp[capacity_]


print(knapsack_iter4([60, 100, 120], [10, 20, 30], 50))
