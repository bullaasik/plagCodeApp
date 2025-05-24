def knapsack_iter(values_, weights_, v3):
    n_ = len(v9)
    dp = [0 for _ in range(capacity_ + 1)]
    for i_ in range(n_):
        for w in range(capacity_, v1[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v1[i_]] + v4[v6])
    return dp[capacity_]
print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
# Comment 31