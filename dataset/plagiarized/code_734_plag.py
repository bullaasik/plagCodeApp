def var_3851(v1, weights_, v9):
    var_2501 = len(var_5371)
    var_7131 = [(0) for var_4395 in range(var_3082 + 1)]
    for var_7200 in range(var_8157):
        for var_4750 in range(var_6070, var_2711[var_6313] - 1, -1):
            var_7131[var_4750] = var_3876(var_7131[var_4750], var_7131[var_4750 - var_2711[var_6313]] + var_2889[var_6313])
    return var_7131[var_6070]


print(var_3851([60, 100, 120], [10, 20, 30], 50))
