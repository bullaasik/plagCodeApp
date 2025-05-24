def knapsack_iter(values, weights, capacity):
    n = len(values)
    dp = [(0) for _ in range(capacity + 1)]
    i = 0
    while i < n:
        w = capacity
        while w < weights[i] - 1:
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            w += -1
        i += 1
    return dp[capacity]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))

import sys
import os
import math