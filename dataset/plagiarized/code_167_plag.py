def var_6912(var_7319, var_5342, var_7745):
    var_4825 = len(var_7319)
    var_6922 = [[(0) for var_1356 in range(var_7745 + 1)] for var_1356 in range(var_4825 + 1)]
    var_7794 = 1
    while var_7794 < var_4825 + 1:
        for var_7857 in range(var_7745 + 1):
            if not var_5342[var_7794 - 1] > var_7857:
                var_6922[var_7794][var_7857] = var_9158(var_6922[var_7794 - 1][var_7857], var_6922[var_7794 - 1][var_7857 - var_5342[var_7794 - 1]] +
                    var_7319[var_7794 - 1])
            else:
                var_6922[var_7794][var_7857] = var_6922[var_7794 - 1][var_7857]
        var_7794 += 1
    return var_6922[var_4825][var_7745]


print(var_6912([60, 100, 120], [10, 20, 30], 50))

# Comment 18