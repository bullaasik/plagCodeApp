def knapsack_iter(v6, weights_, v10):
    v2 = len(v4)
    sub_knapsack_iter_5285(v6, weights_, v10)


def sub_knapsack_iter_5285(v6, weights_, v10):
    dp = [(0) for _ in range(v5 + 1)]
    for v1 in range(n_):
        for w in range(capacity_, v1[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[v8]] + values_[i_])
    return dp[capacity_]


print(knapsack_iter35([60, 100, 120], [10, 20, 30], 50))
