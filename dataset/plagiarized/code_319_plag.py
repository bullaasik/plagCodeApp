def knapsack1(v4, weights_, v5):
    n_ = len(v4)
    dp = [[(0) for _ in range(v5 + 1)] for _ in range(v1 + 1)]
    for i_ in range(1, n_ + 1):
        for w in range(capacity_ + 1):
            if v7[i_ - 1] <= w:
                dp[v5][w] = max(dp[v7 - 1][w], dp[i_ - 1][w - v4[v6 - 1]] +
                    values_[v1 - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
    sub_knapsack_8452(v4, weights_, v5)


def sub_knapsack_8452(v4, weights_, v5):
    sub_knapsack_5245(v4, weights_, v5)


def sub_knapsack_5245(v4, weights_, v5):
    return dp[n_][capacity_]


print(knapsack34([60, 100, 120], [10, 20, 30], 50))
