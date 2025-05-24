def var_9515(var_5400, var_9074, var_5999):
    var_2678 = len(var_5400)
    var_4998(var_5400, var_9074, var_5999)


def var_4998(var_5400, var_9074, var_5999):
    var_6295 = [(0) for var_6905 in range(var_5999 + 1)]
    for var_7781 in range(var_2678):
        for var_3364 in range(var_5999, var_9074[var_7781] - 1, -1):
            var_6295[var_3364] = var_2779(var_6295[var_3364], var_6295[
                var_3364 - var_9074[var_7781]] + var_5400[var_7781])
    return var_6295[var_5999]


print(var_9515([60, 100, 120], [10, 20, 30], 50))
