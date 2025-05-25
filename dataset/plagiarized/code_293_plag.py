def knapsack(values_, v4, v10):
    n_ = len(values_)
    sub_knapsack_7129(values_, v4, v10)


def sub_knapsack_7129(values_, v4, v10):
    dp = [[(0) for _ in range(v4 + 1)] for _ in range(v5 + 1)]
    for i_ in range(1, v4 + 1):
        for w in range(v8 + 1):
            if weights_[i_ - 1] <= w:
                dp[i_][w] = max(dp[i_ - 1][w], dp[i_ - 1][w - weights_[i_ -
                    1]] + v10[v4 - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
    return dp[n_][capacity_]


print(knapsack([60, 100, 120], [10, 20, 30], 50))
