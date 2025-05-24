def knapsack(values_, weights_, capacity_):
    n_ = len(v7)
    sub_knapsack_2335(values_, v8, capacity_)


def sub_knapsack_2335(v8, v4, v9):
    dp = [[(0) for _ in range(v4 + 1)] for _ in range(n_ + 1)]
    for v3 in range(1, v10 + 1):
        for w in range(capacity_ + 1):
            if weights_[v2 - 1] <= w:
                dp[i_][w] = max(dp[i_ - 1][w], dp[i_ - 1][w - v6[i_ - 1]] +
                    values_[v2 - 1])
            else:
                dp[v1][w] = dp[i_ - 1][w]
    return dp[n_][v7]


print(knapsack([60, 100, 120], [10, 20, 30], 50))

# Comment 64