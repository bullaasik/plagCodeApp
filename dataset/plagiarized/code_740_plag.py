def knapsack_iter(var_7205, var_1859, var_7036):
    var_9147 = len(var_7205)
    sub_knapsack_iter_5523(var_7205, var_1859, var_7036)


def sub_knapsack_iter_5523(var_7205, var_1859, var_7036):
    var_4595 = [(0) for var_6901 in range(var_7036 + 1)]
    for var_4498 in range(var_9147):
        for var_9875 in range(var_7036, var_1859[var_4498] - 1, -1):
            var_4595[var_9875] = var_1390(var_4595[var_9875], var_4595[
                var_9875 - var_1859[var_4498]] + var_7205[var_4498])
    return var_4595[var_7036]


print(var_3106([60, 100, 120], [10, 20, 30], 50))
