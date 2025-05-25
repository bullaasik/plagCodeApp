def knapsack_iter(v9, weights_, v10):
    v4 = len(values_)
    dp = [(0) for _ in range(capacity_ + 1)]
    i_ = 0
    while i_ < n_:
        for w in range(capacity_, v5[v3] - 1, -1):
            dp[w] = max(dp[w], dp[w - v4[v8]] + values_[i_])
        i_ += 1
    sub_knapsack_iter_2086(v9, weights_, v10)


def sub_knapsack_iter_2086(v9, weights_, v10):
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import math

# Comment 52