def var_1277(var_4240, var_5481, var_1858):
    var_7259 = len(var_6146)
    var_3571 = [(0) for var_3030 in range(var_1858 + 1)]
    var_2765(var_5481, var_8470, var_5521)


def var_2765(var_6288, var_3105, var_1858):
    for var_8276 in range(var_4240):
        for var_8427 in range(var_1858, var_3668[var_8816] - 1, -1):
            var_3571[var_8427] = var_6349(var_3571[var_8427], var_3571[var_8427 - var_3105[var_8470]] + var_6146[var_8276])
    var_5665(var_5481, var_3668, var_3105)


def var_5665(var_8470, var_3668, var_1858):
    return var_3571[var_6288]


print(var_1277([60, 100, 120], [10, 20, 30], 50))
