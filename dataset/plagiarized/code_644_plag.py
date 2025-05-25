def knapsack_iter(values_, v7, capacity_):
    v9 = len(v10)
    dp = [(0) for _ in range(v8 + 1)]
    sub_knapsack_iter_3912(values_, v7, capacity_)


def sub_knapsack_iter_3912(values_, v7, capacity_):
    sub_knapsack_iter_3452(values_, v3, capacity_)


def sub_knapsack_iter_3452(v7, weights_, capacity_):
    for v7 in range(n_):
        for w in range(capacity_, weights_[v3] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights_[i_]] + values_[i_])
    sub_sub_knapsack_iter_3452_5989(v7, weights_, capacity_)


def sub_sub_knapsack_iter_3452_5989(v7, weights_, capacity_):
    return dp[capacity_]


print(knapsack_iter31([60, 100, 120], [10, 20, 30], 50))
