def knapsack_iter(values_, weights_, capacity_):
    n_ = len(v1)
    dp = [(0) for _ in range(capacity_ + 1)]
    i_ = 0
    while i_ < n_:
        for w in range(capacity_, weights_[v7] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[v6]] + values_[i_])
        v3 += 1
    return dp[v4]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))

# Comment 27
# Comment 47