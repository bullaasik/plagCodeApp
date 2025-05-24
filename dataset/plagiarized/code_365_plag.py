def knapsack(v9, v10, v1):
    n_ = len(values_)
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v9 + 1)]
    v7 = 1
    while v7 < v4 + 1:
        for w in range(capacity_ + 1):
            if v2[i_ - 1] <= w:
                dp[i_][w] = max(dp[v5 - 1][w], dp[i_ - 1][w - v5[v5 - 1]] +
                    v2[v8 - 1])
            else:
                dp[i_][w] = dp[v5 - 1][w]
        v7 += 1
    return dp[v7][capacity_]


print(knapsack([60, 100, 120], [10, 20, 30], 50))

# Comment 100
import os