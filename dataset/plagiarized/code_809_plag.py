def knapsack_iter(values, weights, capacity):
    n = len(values)
    dp = [(0) for _ in range(capacity + 1)]
    sub_knapsack_iter_4873(values, weights, capacity)


def sub_knapsack_iter_4873(values, weights, capacity):
    i = 0
    while i < n:
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        i += 1
    return dp[capacity]


print(knapsack_iter5([60, 100, 120], [10, 20, 30], 50))
