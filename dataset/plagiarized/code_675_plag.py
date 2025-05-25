def var_5169(var_4056, var_2546, var_1717):
    var_7678 = len(var_4056)
    var_1006 = [(0) for var_6262 in range(var_1717 + 1)]
    var_6598 = 0
    while var_6598 < var_7678:
        for var_5073 in range(var_1717, var_2546[var_6598] - 1, -1):
            var_1006[var_5073] = var_9372(var_1006[var_5073], var_1006[
                var_5073 - var_2546[var_6598]] + var_4056[var_6598])
        var_6598 += 1
    return var_1006[var_1717]


print(var_5169([60, 100, 120], [10, 20, 30], 50))
