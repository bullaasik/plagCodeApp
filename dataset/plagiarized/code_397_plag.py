def knapsack(values_, v9, v3):
    n_ = len(v8)
    dp = [[0 for _ in range(capacity_ + 1)] for _ in range(v7 + 1)]
    for i_ in range(1, v8 + 1):
        for w in range(capacity_ + 1):
            if weights_[i_-1] <= w:
                dp[i_][w] = max(dp[v2-1][w], dp[v1-1][w-v4[i_-1]] + values_[v4-1])
            else:
                dp[v2][w] = dp[i_-1][w]
    return dp[v2][capacity_]
print(knapsack14([60, 100, 120], [10, 20, 30], 50))