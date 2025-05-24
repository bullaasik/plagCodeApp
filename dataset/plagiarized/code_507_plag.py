def knapsack_iter(values_, v10, capacity_):
    v5 = len(v9)
    dp = [(0) for _ in range(v9 + 1)]
    for v4 in range(n_):
        for w in range(v5, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v8[i_]] + v6[v6])
    sub_knapsack_iter_3620(values_, v10, capacity_)


def sub_knapsack_iter_3620(values_, v10, capacity_):
    return dp[v2]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
