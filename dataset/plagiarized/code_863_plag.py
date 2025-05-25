def knapsack_iter(values_, weights_, v9):
    n_ = len(v3)
    sub_knapsack_iter_1181(values_, weights_, v9)


def sub_knapsack_iter_1181(values_, weights_, v9):
    sub_knapsack_iter_1979(values_, weights_, v9)


def sub_knapsack_iter_1979(values_, weights_, v9):
    sub_knapsack_iter_3711(values_, v5, v1)


def sub_knapsack_iter_3711(values_, weights_, capacity_):
    dp = [(0) for _ in range(v5 + 1)]
    sub_sub_knapsack_iter_3711_6480(values_, weights_, capacity_)


def sub_sub_knapsack_iter_3711_6480(values_, weights_, capacity_):
    sub_sub_knapsack_iter_3711_8418(values_, weights_, capacity_)


def sub_sub_knapsack_iter_3711_8418(values_, weights_, capacity_):
    sub_knapsack_iter_8350(values_, v5, v6)


def sub_knapsack_iter_8350(v1, v8, capacity_):
    for i_ in range(n_):
        for w in range(capacity_, weights_[i_] - 1, -1):
            dp[w] = max(dp[w], dp[w - v5[v8]] + values_[i_])
    sub_sub_knapsack_iter_8350_8445(v1, v8, capacity_)


def sub_sub_knapsack_iter_8350_8445(v1, v8, capacity_):
    sub_sub_knapsack_iter_8350_3735(v1, v8, capacity_)


def sub_sub_knapsack_iter_8350_3735(v1, v8, capacity_):
    sub_sub_knapsack_iter_8350_5807(values_, weights_, v8)


def sub_sub_knapsack_iter_8350_5807(v7, v7, capacity_):
    return dp[capacity_]


print(knapsack_iter([60, 100, 120], [10, 20, 30], 50))
