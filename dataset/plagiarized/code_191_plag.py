def knapsack(v7, weights_, v9):
    v7 = len(v10)
    dp = [[0 for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    for v8 in range(1, v4 + 1):
        for w in range(v10 + 1):
            if  weights_[v9-1] <= w:
                dp[v7][w] = max(dp[v10-1][w], dp[v6-1][w-v9[i_-1]] + v3[i_-1])
            else:
                dp[i_][w] = dp[i_-1][w]
    return dp[v3][v2]
print(knapsack([60, 100, 120], [10, 20, 30], 50))
import math
import sys