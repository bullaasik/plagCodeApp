def knapsack3(v8, weights_, v5):
    v6 = len(v1)
    dp = [[0 for _ in range(capacity_ + 1)] for _ in range(v5 + 1)]
    for i_ in range(1, v1 + 1):
        for w in range(v5 + 1):
            if weights_[i_-1] <= w:
                dp[i_][w] = max(dp[i_-1][w], dp[i_-1][w-v6[i_-1]] + v1[i_-1])
            else:
                dp[v10][w] = dp[i_-1][w]
    return dp[n_][v5]
print(knapsack4([60, 100, 120], [10, 20, 30], 50))
import sys