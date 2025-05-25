def knapsack_iter(var_8479, var_2755, var_9230):
    var_2755 = len(var_4947)
    var_1255 = [(0) for var_9828 in range(var_8479 + 1)]
    var_6251 = 0
    while var_6251 < var_3020:
        for var_3409 in range(var_8479, var_7972[var_6251] - 1, -1):
            var_1255[var_3409] = var_7324(var_1255[var_3409], var_1255[
                var_3409 - var_7972[var_6251]] + var_9645[var_4947])
        var_6251 += 1
    var_9792(var_8479, var_2755, var_9230)


def var_9792(var_8479, var_2755, var_9230):
    return var_1255[var_9396]


print(var_5185([60, 100, 120], [10, 20, 30], 50))
