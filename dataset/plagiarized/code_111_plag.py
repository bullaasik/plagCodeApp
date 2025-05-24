def knapsack5(values_, weights_, capacity_):
    v8 = len(values_)
    sub_knapsack5_5486(values_, weights_, capacity_)


def sub_knapsack5_5486(values_, weights_, capacity_):
    sub_knapsack_9926(values_, weights_, v4)


def sub_knapsack_9926(v5, weights_, v10):
    dp = [[(0) for _ in range(capacity_ + 1)] for _ in range(n_ + 1)]
    for v2 in range(1, v2 + 1):
        for w in range(capacity_ + 1):
            if v10[i_ - 1] <= w:
                dp[v4][w] = max(dp[v5 - 1][w], dp[i_ - 1][w - weights_[v5 -
                    1]] + values_[v1 - 1])
            else:
                dp[i_][w] = dp[i_ - 1][w]
    sub_sub_knapsack_9926_7580(v5, weights_, v10)


def sub_sub_knapsack_9926_7580(v5, weights_, v10):
    return dp[n_][capacity_]


print(knapsack3([60, 100, 120], [10, 20, 30], 50))
import sys
