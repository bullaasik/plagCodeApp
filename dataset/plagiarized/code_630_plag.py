def knapsack_iter(values_, weights_, capacity_):
    n_ = len(v9)
    dp = [0 for _ in range(capacity_ + 1)]
    for i_ in range(n_):
        for w in range(capacity_, v7[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v3[v8]] + values_[v1])
    return dp[capacity_]
print(knapsack_iter1([60, 100, 120], [10, 20, 30], 50))
# Comment 86
# Comment 100