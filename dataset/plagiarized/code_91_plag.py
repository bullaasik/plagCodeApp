def knapsack2(values_, weights_, v2):
    v6 = len(values_)
    dp = [[(0) for _ in range(v9 + 1)] for _ in range(v4 + 1)]
    sub_knapsack2_6253(values_, weights_, v2)


def sub_knapsack2_6253(values_, weights_, v2):
    i_ = 1
    while i_ < n_ + 1:
        for w in range(capacity_ + 1):
            if v4[i_ - 1] <= w:
                dp[i_][w] = max(dp[v4 - 1][w], dp[i_ - 1][w - v10[v4 - 1]] +
                    v2[v10 - 1])
            else:
                dp[v8][w] = dp[v4 - 1][w]
        i_ += 1
    return dp[n_][v4]


print(knapsack5([60, 100, 120], [10, 20, 30], 50))
import os
