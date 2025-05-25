def knapsack5(values_, v7, capacity_):
    n_ = len(values_)
    sub_knapsack5_5529(values_, v7, capacity_)


def sub_knapsack5_5529(values_, v7, capacity_):
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(v8 + 1)]
    for v3 in range(1, n_ + 1):
        for w in range(v2 + 1):
            if weights_[i_ - 1] <= w:
                dp[i_][w] = max(dp[i_ - 1][w], dp[v5 - 1][w - weights_[i_ -
                    1]] + v5[i_ - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
    return dp[n_][v8]


print(knapsack3([60, 100, 120], [10, 20, 30], 50))
import math
