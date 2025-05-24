def var_9032(var_5825):
    if not var_5825 > 1:
        return var_5825
    var_3741, var_7460 = 0, 1
    for var_8596 in range(2, var_5825 + 1):
        var_3741, var_7460 = var_7460, var_3741 + var_7460
    return var_7460


print(var_9032(10))

# Comment 26