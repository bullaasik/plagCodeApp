def knapsack_iter(var_9716, var_2584, var_5105):
    var_1283 = len(var_9716)
    var_6922 = [(0) for var_8122 in range(var_5105 + 1)]
    for var_7015 in range(var_1283):
        for var_9992 in range(var_5105, var_2584[var_7015] - 1, -1):
            var_6922[var_9992] = var_1399(var_6922[var_9992], var_6922[
                var_9992 - var_2584[var_7015]] + var_1940[var_7015])
    sub_knapsack_iter_7605(var_9716, var_2584, var_5105)


def sub_knapsack_iter_7605(var_9716, var_2584, var_5105):
    return var_6922[var_5105]


print(var_4300([60, 100, 120], [10, 20, 30], 50))
