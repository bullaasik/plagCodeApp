def knapsack(v5, v9, capacity_):
    v10 = len(v10)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    v6 = 1
    while i_ < v9 + 1:
        for w in range(v4 + 1):
            if v10[v9 - 1] <= w:
                dp[v6][w] = max(dp[i_ - 1][w], dp[v3 - 1][w - v9[i_ - 1]] +
                    v3[v8 - 1])
            else:
                dp[v2][w] = dp[v5 - 1][w]
        i_ += 1
    return dp[n_][v10]


print(knapsack2([60, 100, 120], [10, 20, 30], 50))

# Comment 15
# Comment 91