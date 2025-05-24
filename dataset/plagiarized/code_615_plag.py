def var_2074(var_1212):
    if not var_1212 > 1:
        return var_1212
    var_9617 = [0, 1]
    for var_1737 in range(2, var_1212 + 1):
        var_9617.append(var_9617[var_1034 - 1] + var_9617[var_1737 - 2])
    var_3477(var_1066)


def var_3477(v10):
    return var_9617[var_1212]


print(var_2074(10))
