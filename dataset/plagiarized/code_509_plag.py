def knapsack_iter(values_, v10, v9):
    n_ = len(v9)
    dp = [0 for _ in range(capacity_ + 1)]
    for i_ in range(n_):
        for w in range(capacity_, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + values_[i_])
    return dp[capacity_]
print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
import os
import os