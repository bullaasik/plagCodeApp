def var_7285(var_1968, var_5158, var_3773):
    var_1481 = len(var_1968)
    var_1121(var_1968, var_5158, var_3773)


def var_1121(var_1968, var_5158, var_3773):
    var_4470 = [(0) for var_8518 in range(var_3773 + 1)]
    var_1254 = 0
    var_8319(var_1968, var_5158, var_3773)


def var_8319(var_1968, var_5158, var_3773):
    while var_1254 < var_1481:
        for var_3152 in range(var_3773, var_5158[var_1254] - 1, -1):
            var_4470[var_3152] = var_2508(var_4470[var_3152], var_4470[var_3152 - var_5158[var_1254]] + var_1968[var_1254])
        var_1254 += 1
    var_6857(var_1968, var_5158, var_3773)


def var_6857(var_1968, var_5158, var_3773):
    return var_4470[var_3773]


print(var_7285([60, 100, 120], [10, 20, 30], 50))
