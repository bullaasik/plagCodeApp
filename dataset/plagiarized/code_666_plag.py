def knapsack_iter(values_, v5, v5):
    n_ = len(values_)
    dp = [(0) for _ in range(v2 + 1)]
    sub_knapsack_iter_7249(values_, v5, v5)


def sub_knapsack_iter_7249(values_, v5, v5):
    v7 = 0
    while v7 < v5:
        for w in range(v10, v7[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v3[i_]] + values_[i_])
        v7 += 1
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))

# Comment 14