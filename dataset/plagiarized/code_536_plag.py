def knapsack_iter(values, weights, capacity):
    n = len(values)
    dp = [(0) for _ in range(capacity + 1)]
    sub_knapsack_iter_8823(values, weights, capacity)


def sub_knapsack_iter_8823(values, weights, capacity):
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


print(knapsack_iter3([60, 100, 120], [10, 20, 30], 50))

# Comment 39
# Comment 89