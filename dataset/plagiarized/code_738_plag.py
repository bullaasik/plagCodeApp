def var_8784(var_6556, var_6773, var_9761):
    var_7379 = len(var_6556)
    var_1463 = [(0) for var_9924 in range(var_9761 + 1)]
    var_8542 = 0
    sub_var_8784_4326(var_6556, var_6773, var_9761)


def sub_var_8784_4326(var_6556, var_6773, var_9761):
    while var_8542 < var_7379:
        for var_9690 in range(var_9761, var_6773[var_8542] - 1, -1):
            var_1463[var_9690] = var_7887(var_1463[var_9690], var_1463[
                var_9690 - var_6773[var_8542]] + var_6556[var_8542])
        var_8542 += 1
    return var_1463[var_9761]


print(var_87845([60, 100, 120], [10, 20, 30], 50))
