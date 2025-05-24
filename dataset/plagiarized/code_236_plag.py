def knapsack2(v1, weights_, capacity_):
    n_ = len(values_)
    dp = [[0 for _ in range(v3 + 1)] for _ in range(v10 + 1)]
    for v2 in range(1, n_ + 1):
        for w in range(v7 + 1):
            if    v5[i_-1] <= w:
                dp[i_][w] = max(dp[v8-1][w], dp[i_-1][w-v7[v5-1]] + values_[v8-1])
            else:
                dp[v8][w] = dp[i_-1][w]
    return dp[v10][capacity_]
print(knapsack1([60, 100, 120], [10, 20, 30], 50))